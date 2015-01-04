from setuptools import setup, Extension

setup (name = 'ipvs',
	version = '1.0',
	description = 'Python wrapper for IPVS',
	author = 'Ruben Kerkhof',
	author_email = '<ruben@tilaa.com',
	ext_modules = [
		Extension(
			'ipvs',
			sources = [
				'src/ipvsmodule.c',
				'src/libipvs.c',
				'src/ip_vs_nl_policy.c',
			],
			include_dirs = ['/usr/include/libnl3'],
			libraries = ['nl-3', 'nl-genl-3'],
			define_macros = [('LIBIPVS_USE_NL',1)],
		),
	],
	test_suite = "test_ipvs",
)
