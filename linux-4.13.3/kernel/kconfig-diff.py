#!/usr/bin/ipython2 -i
"""
This script should be run from a folder residing at the toplevel of the kernel source tree, and which also contains

	https://raw.github.com/ulfalizer/Kconfiglib/master/kconfiglib.py

Invoke as follows:

	./kconfig-diff.py x86 DEFAULT kern1.conf kern2.conf kern3.conf

You can pass up to four arguments after the architecture; these should be paths of kernel config files, or the keyword
DEFAULT for the default kernel settings. The latter can be used only in the first slot.

Running the script will start an interactive IPython session (or you can change the shebang line to make it a plain Python session)
pre-loaded with kconfiglib.Config objects representing the different configs.

Some sample operations:

	>>> DEFAULT, kern1, kern2, kern3

	(<kconfiglib.Config instance at 0x977970c>,
	<kconfiglib.Config instance at 0xb6ad36c>,
	<kconfiglib.Config instance at 0xd820a6c>,
	<kconfiglib.Config instance at 0xf98f62c>)

kern1.conf and kernelconfig.kern1 both get saved as the global object 'kern1'; otherwise, refer to the Config objects as one, two, ...

	>>> one_s, one_c = kern1.diffs
	>>> two_s, two_c = kern2.diffs
	>>> three_s, three_c = kern3.diffs
	>>> map(len,[one_s, one_c, two_s, two_c, three_s, three_c])
	[2946, 25, 331, 6, 1469, 10]

This indicates that kern1 differs from the DEFAULT settings in 2946 modifiable symbols and 25 modifiable choices. Differences which are forced
by other selections aren't included here; only differences that could be immediately changed. If the DEFAULT config was selected, only the first
succeeding config is compared to it. Otherwise, configs are compared to all of the configurations that precede them in the argv list: so
kern2 is compared to kern1, and kern3 is compared to both kern2 and kern1. Hence the lengths 1496, 10 for kern3 indicate that that there are 1496
modifiable symbols where kern3 differs from one or both of kern1 and kern2, and 10 modifiable choices where it differs from them.

The elements in the lists three_s and three_c are strings, that look like this:

	>>> print three_s[0]
	Symbol RD_BZIP2
	Type           : bool
	Value          : "n"
	User value     : "n"
	Kern2 config   : 'n'
	Kern1 config   : 'y'
	Visibility     : "y"
	 General setup
	Is choice item : false
	Is defined     : true
	Is from env.   : false
	Is special     : false
	Prompts:
	 "Support initial ramdisks compressed using bzip2" if EXPERT && BLK_DEV_INITRD (value: "y")
	Default values:
	 !EXPERT (value: "n")
	  Condition: BLK_DEV_INITRD (value: "y")
	Selects:
	 DECOMPRESS_BZIP2 if BLK_DEV_INITRD (value: "y")
	Reverse dependencies:
	 (no reverse dependencies)
	Additional dependencies from enclosing menus and if's:
	 BLK_DEV_INITRD (value: "y")
	Locations: ../usr/Kconfig:57
	
	Support loading of a bzip2 encoded initial ramdisk or cpio buffer
	If unsure, say N.

Notice the lines "Value" and "User value". The "User value" is a legal setting in the config file for the given symbol type; however, it may not be honored depending on other configuration selections. "Value" is what will really be honored (and displayed in the kernel `make menuconfig` display). Notice also that the Values for kern2 and kern1 are displayed here. One of these will differ from the Value for kern3, or this entry wouldn't have been added to kern3.diffs[0].

Choices are formatted a bit differently:

	>>> print three_c[0]
	Choice
	Name (for named choices): (no name)
	Type            : bool
	Selected symbol : DEFAULT_DEADLINE
	User value      : DEFAULT_DEADLINE
	Kern2 config    : DEFAULT_CFQ
	Kern1 config    : DEFAULT_CFQ
	Mode            : "y"
	Visibility      : "y"
	 IO Schedulers
	Optional        : false
	Prompts:
	 "Default I/O scheduler"
	Defaults:
	 DEFAULT_CFQ
	Choice symbols:
	 DEFAULT_DEADLINE DEFAULT_CFQ DEFAULT_NOOP
	Additional dependencies from enclosing menus and if's:
	 BLOCK (value: "y")
	Locations: ../block/Kconfig.iosched:42
	
	Select the I/O scheduler which will be used by default for all
	block devices.


See the below source, run `pydoc kconfiglib`, and see https://github.com/ulfalizer/Kconfiglib/tree/master/examples
for more information.
"""

print
import os, sys
from collections import defaultdict

try:
	with open('../Makefile') as f:
		version = []
		line = f.readline()
		if not line.startswith('VERSION ='):
			raise IOError
		version.append(line[10:-1])
		line = f.readline()
		if not line.startswith('PATCHLEVEL ='):
			raise IOError
		line = line[13:-1] or '0'
		version.append(line)
		line = f.readline()
		if not line.startswith('SUBLEVEL ='):
			raise IOError
		line = line[11:-1] or '0'
		version.append(line)
		line = f.readline()
		if not line.startswith('EXTRAVERSION ='):
			raise IOError
		line = line[15:-1]
		if line:
			version.append(line)
		version = '.'.join(version)
except IOError:
	print >> sys.stderr, "Parent directory is not a kernel source tree."
	sys.exit(1)

argv = sys.argv
assert argv[1] == 'x86' or argv[1] == 'x86_64', "First argument should be x86 or x86_64"
os.environ.update({'srctree':'..','SRCARCH':argv[1],'ARCH':argv[1],'KERNELVERSION':version})

# sys.path.insert(0, '../Kconfiglib')
import kconfiglib as K

def f(self, x):
	assert x.is_choice()
	xn = x.symbol_names
	for y in self.get_choices():
		res = len(xn.intersection(y.symbol_names))
		# res = xn == y.symbol_names
		if res:
			return y
K.Config.get_choice = f
# instance.get_choice = types.MethodType(K_get_choice, instance, K)

def f(self):
	d = defaultdict(lambda: None)
	for x in self.get_choices():
		d[x.symbol_names] = x
	return d
K.Config.get_choice_dict = f

def f(self):
	ps = []
	p = self.get_parent()
	while p is not None:
		ps.insert(0, p)
		p = p.get_parent()
	return ps
K.Item.get_parents = f

del f

argv = argv[2:]
if len(argv) < 2 or len(argv) > 4:
	print >> sys.stderr, "Supply 2-4 kernel configs (or DEFAULT) to compare."
	sys.exit(1)
	
G = globals()
for i,p in enumerate(argv):
	k = K.Config('../Kconfig')
	k.config_path = p
	if p == 'DEFAULT':
		assert i==0, "DEFAULT config should be specified first."
		k.config_name = 'DEFAULT'
		G['DEFAULT'] = k
	else:
		print("loading {0}...".format(p))
		k.load_config(p)
		p = p.split('/')[-1]
		if p.startswith('kernelconfig.'):
			k.config_name = p[13:]
			try:
				G[k.config_name] = k
			except IOError:
				pass
		elif p.endswith('.conf'):
			k.config_name = p[:-5]
			try:
				G[k.config_name] = k
			except IOError:
				pass
		else:
			k.config_name = p
	k.choice_symbols=[]
	k.non_choice_symbols=[]
	for sym in k:
		(k.choice_symbols if sym.is_choice_symbol() else k.non_choice_symbols).append(sym)
	for s in k.non_choice_symbols:
		s.others = {}
	for c in k.get_choices():
		c.symbol_names = frozenset(s.get_name() for s in c.get_symbols())
		sel = c.get_selection()
		c.sel_name = sel.get_name() if sel else None
		c.others = {}
	argv[i] = k

if len(argv) == 2:
	one, two = argv
elif len(argv) == 3:
	one, two, three = argv
elif len(argv) == 4:
	one, two, three, four = argv




def cmp_symbols(s, t):
	assert s.is_symbol() and t.is_symbol()
	sv, tv = s.get_value(), t.get_value()
	if sv == tv:
		return False
	elif not s.is_modifiable():
		return 0
	elif s.get_type() in (K.TRISTATE, K.BOOL):
		u, l = s.get_upper_bound(), s.get_lower_bound()
		if K.tri_less(tv, l) and not K.tri_greater(sv, l):
			return "pinlow"
		elif K.tri_greater(tv, u) and not K.tri_less(sv, u):
			return "pinhi"
	return True # values are deliberately different

def cmp_choices(c, d):
	assert c.is_choice() and d.is_choice()
	cm, dm = c.get_mode(), d.get_mode()
	if cm != dm:
		return 0 if cm == 'n' or c.get_visibility() == 'n'  else True
	if cm == 'n':
		return False
	elif cm == 'y':
		return c.sel_name != d.sel_name
	else:
		assert cm == 'm'
		cs = set(s.get_name() for s in c.get_symbols() if s.get_value() == 'm')
		ds = set(s.get_name() for s in d.get_symbols() if s.get_value() == 'm')
		return cs != ds


def cmp_all(xk, yk):
	xname = xk.config_name
	yname = yk.config_name
	for y in yk.non_choice_symbols:
		y.others[xname] = None
	
	for x in xk.non_choice_symbols:
		y = yk.get_symbol(x.get_name())
		if y is None:
			# symbol in xk but not yk
			x.others[yname] = None
		else:
			res = cmp_symbols(x, y)
			x.others[yname] = y.others[xname] = res
	for y in yk.get_choices():
		y.others[xname] = (None, None, None)
	yc = yk.get_choice_dict()
	for x in xk.get_choices():
		# at least in kernel 3.9.2, choice_symbols are always BOOL or TRISTATE
		y = yc[x.symbol_names]
		if y is None:
			# choice in xk but not yk
			x.others[yname] = (None, None, None)
		else:
			res = cmp_choices(x, y)
			x.others[yname] = (res, y, y.sel_name)
			y.others[xname] = (res, x, x.sel_name)


argv[0].bad_symbols = frozenset([])
argv[0].bad_choices = frozenset([])

for j in range(1, len(argv)):
	jk = argv[j]
	jk.bad_symbols = set()
	jk.bad_choices = set()
	for i in range(0, j):
		ik = argv[i]
		if j > 1 and ik.config_name == 'DEFAULT':
			continue
		print "comparing {0} and {1}...".format(jk.config_name, ik.config_name)
		cmp_all(jk, ik)
		jk.bad_symbols.update(s.get_name() for s in jk.non_choice_symbols if s.others[ik.config_name] or s.get_name() in ik.bad_symbols)
		jk.bad_choices.update(c.symbol_names for c in jk.get_choices() if c.others[ik.config_name][0] or c.symbol_names in ik.bad_choices)
	# take symbol objects, in original order
	js = [s for s in jk.non_choice_symbols if s.get_name() in jk.bad_symbols]
	# take choice objects, in original order
	jc = [c for c in jk.get_choices() if c.symbol_names in jk.bad_choices]
	if j == 1 and argv[0].config_name == 'DEFAULT':
		jk.bad_symbols = argv[0].bad_symbols
		jk.bad_choices = argv[0].bad_choices
	# jsymbols holds non-choice symbol diffs
	jsymbols = []
	for s in js:
		sz = str(s).splitlines()
		sname = s.get_name()
		# sz.insert(5, "Location       :")
		pars = [p.get_title() for p in s.get_parents()]
		for i,p in enumerate(pars):
			pars[i] = ' '*(i+1)+p
		sz[5:5] = pars
		# for i in range(j-1, -1, -1):
		for i in range(0, j):
			ik = argv[i]
			iname = ik.config_name
			if j > 1 and ik.config_name == 'DEFAULT':
				continue
			t = ik.get_symbol(sname)
			sz.insert(4, '{0} config {1}: {2}'.format(iname.title(), ' '*(7-len(iname)), repr(t.get_value()) if t else 'None'))
		txt = '\n'.join(sz)
		h = s.get_help()
		if h:
			txt = txt + '\n\n' + h
		jsymbols.append(txt)
	# jchoices holds choice diffs
	jchoices = []
	for c in jc:
		cz = str(c).splitlines()
		# cz.insert(7, "Location        :")
		pars = [p.get_title() for p in c.get_parents()]
		for i,p in enumerate(pars):
			pars[i] = ' '*(i+1)+p
		cz[7:7] = pars
		# for i in range(j-1, -1, -1):
		for i in range(0, j):
			ik = argv[i]
			if j > 1 and ik.config_name == 'DEFAULT':
				continue
			iname = ik.config_name
			(_,_,sel) = c.others[iname]
			cz.insert(5, "{0} config {1}: {2}".format(iname.title(), ' '*(8-len(iname)), sel if sel else 'None'))
		txt = '\n'.join(cz)
		h = c.get_help()
		if h:
			txt = txt + '\n\n' + h
		jchoices.append(txt)
	jk.diffs = (jsymbols, jchoices)
