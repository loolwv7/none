#format wiki
#languge zh

Strace how to
<<TableOfContents>>

== Example 01 ==

firefox
{{{
strace -ff -t -p `ps -ef|grep -v grep|grep java|awk '{ print $2 }'` -o web
}}}
then
grep open web.*
{{{
ldd /home/merlyn/.webex/1324/atasjni 
ERROR: ld.so: object '/usr/lib64/libswmhack.so.0.0' from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS64): ignored.
	libX11.so.6 => not found
	libXt.so.6 => not found
	libXext.so.6 => not found
	libXi.so.6 => not found
	libXmu.so.6 => not found
	libdl.so.2 => /lib32/libdl.so.2 (0xf77a3000)
	libpthread.so.0 => /lib32/libpthread.so.0 (0xf7789000)
	libgtk-x11-2.0.so.0 => not found
	libgdk-x11-2.0.so.0 => not found
	libatk-1.0.so.0 => not found
	libgdk_pixbuf-2.0.so.0 => not found
	libpangoxft-1.0.so.0 => not found
	libpangox-1.0.so.0 => not found
	libpango-1.0.so.0 => not found
	libgobject-2.0.so.0 => not found
	libgmodule-2.0.so.0 => not found
	libglib-2.0.so.0 => not found
	libstdc++.so.6 => /usr/lib/gcc/x86_64-pc-linux-gnu/4.8.4/32/libstdc++.so.6 (0xf769e000)
	libm.so.6 => /lib32/libm.so.6 (0xf7657000)
	libgcc_s.so.1 => /usr/lib/gcc/x86_64-pc-linux-gnu/4.8.4/32/libgcc_s.so.1 (0xf763c000)
	libc.so.6 => /lib32/libc.so.6 (0xf749d000)
	/lib/ld-linux.so.2 (0xf77ca000)
}}}

=== install missing lib ===
{{{
ABI_X86=32 emerge -va x11-libs/pangox-compat
emerge emul-linux-x86-gtklibs
}}}

{{{
ldd /home/merlyn/.webex/1324/atasjni 
ERROR: ld.so: object '/usr/lib64/libswmhack.so.0.0' from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS64): ignored.
	libX11.so.6 => /usr/lib32/libX11.so.6 (0xf75be000)
	libXt.so.6 => not found
	libXext.so.6 => /usr/lib32/libXext.so.6 (0xf75ab000)
	libXi.so.6 => not found
	libXmu.so.6 => not found
	libdl.so.2 => /lib32/libdl.so.2 (0xf75a5000)
	libpthread.so.0 => /lib32/libpthread.so.0 (0xf758b000)
	libgtk-x11-2.0.so.0 => not found
	libgdk-x11-2.0.so.0 => not found
	libatk-1.0.so.0 => not found
	libgdk_pixbuf-2.0.so.0 => not found
	libpangoxft-1.0.so.0 => /usr/lib32/libpangoxft-1.0.so.0 (0xf7581000)
	libpangox-1.0.so.0 => /usr/lib32/libpangox-1.0.so.0 (0xf7562000)
	libpango-1.0.so.0 => /usr/lib32/libpango-1.0.so.0 (0xf7517000)
	libgobject-2.0.so.0 => /usr/lib32/libgobject-2.0.so.0 (0xf74c3000)
	libgmodule-2.0.so.0 => /usr/lib32/libgmodule-2.0.so.0 (0xf74be000)
	libglib-2.0.so.0 => /usr/lib32/libglib-2.0.so.0 (0xf7382000)
	libstdc++.so.6 => /usr/lib/gcc/x86_64-pc-linux-gnu/4.8.4/32/libstdc++.so.6 (0xf7299000)
	libm.so.6 => /lib32/libm.so.6 (0xf7253000)
	libgcc_s.so.1 => /usr/lib/gcc/x86_64-pc-linux-gnu/4.8.4/32/libgcc_s.so.1 (0xf7237000)
	libc.so.6 => /lib32/libc.so.6 (0xf7098000)
	libxcb.so.1 => /usr/lib32/libxcb.so.1 (0xf7075000)
	/lib/ld-linux.so.2 (0xf771a000)
	libpangoft2-1.0.so.0 => /usr/lib32/libpangoft2-1.0.so.0 (0xf7061000)
	libXft.so.2 => /usr/lib32/libXft.so.2 (0xf704b000)
	libXrender.so.1 => /usr/lib32/libXrender.so.1 (0xf7040000)
	libfontconfig.so.1 => /usr/lib32/libfontconfig.so.1 (0xf7003000)
	libffi.so.6 => /usr/lib32/libffi.so.6 (0xf6ffb000)
	libXau.so.6 => /usr/lib32/libXau.so.6 (0xf6ff7000)
	libXdmcp.so.6 => /usr/lib32/libXdmcp.so.6 (0xf6ff0000)
	libharfbuzz.so.0 => /usr/lib32/libharfbuzz.so.0 (0xf6f94000)
	libfreetype.so.6 => /usr/lib32/libfreetype.so.6 (0xf6eef000)
	libexpat.so.1 => /usr/lib32/libexpat.so.1 (0xf6ec6000)
	libgraphite2.so.3 => /usr/lib32/libgraphite2.so.3 (0xf6ea6000)
	libz.so.1 => /lib32/libz.so.1 (0xf6e8f000)
	libbz2.so.1 => /usr/lib32/libbz2.so.1 (0xf6e7c000)
	libpng16.so.16 => /usr/lib32/libpng16.so.16 (0xf6e43000)
}}}

ABI_X86="32 64" emerge -va x11-libs/libXt x11-libs/libXmu x11-libs/gdk-pixbuf dev-libs/atk



=== add conflict USE flag ===
{{{

x11-libs/gdk-pixbuf:2

  (x11-libs/gdk-pixbuf-2.30.8:2/2::gentoo, ebuild scheduled for merge) pulled in by
    x11-libs/gdk-pixbuf (Argument)

  (x11-libs/gdk-pixbuf-2.30.8:2/2::gentoo, installed) pulled in by
    >=x11-libs/gdk-pixbuf-2.30:2[introspection?,X?,abi_x86_32(-)?,abi_x86_64(-)?,abi_x86_x32(-)?,abi_mips_n32(-)?,abi_mips_n64(-)?,abi_mips_o32(-)?,abi_ppc_32(-)?,abi_ppc_64(-)?,abi_s390_32(-)?,abi_s390_64(-)?] required by (x11-libs/gtk+-3.14.9:3/3::gentoo, installed)
                                 ^^^^^^^^^^^^^^                                                                                                                                                                                                                                                                 
    >=x11-libs/gdk-pixbuf-2.30.7:2[introspection?,abi_x86_32(-)?,abi_x86_64(-)?,abi_x86_x32(-)?,abi_mips_n32(-)?,abi_mips_n64(-)?,abi_mips_o32(-)?,abi_ppc_32(-)?,abi_ppc_64(-)?,abi_s390_32(-)?,abi_s390_64(-)?] required by (x11-libs/gtk+-2.24.27:2/2::gentoo, installed)
                                   ^^^^^^^^^^^^^^                                                                                                                                                                                                                                                               


It might be possible to solve this slot collision
by applying all of the following changes:
   - x11-libs/gdk-pixbuf-2.30.8 (Change USE: +introspection)

}}}
