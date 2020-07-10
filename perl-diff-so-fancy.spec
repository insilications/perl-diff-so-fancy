#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : perl-diff-so-fancy
Version  : 20.06.02
Release  : 1
URL      : file:///insilications/build/clearlinux/packages/perl-diff-so-fancy/perl-diff-so-fancy-20.06.02.tar
Source0  : file:///insilications/build/clearlinux/packages/perl-diff-so-fancy/perl-diff-so-fancy-20.06.02.tar
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-diff-so-fancy-bin = %{version}-%{release}
Requires: git
Requires: git-archive-all
Requires: python3-core
Requires: urllib3
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : git-archive-all
BuildRequires : perl-fatpacker
BuildRequires : perl-fatpacker-perl
BuildRequires : python3-core
BuildRequires : urllib3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# diff-so-fancy  [![Circle CI build](https://circleci.com/gh/so-fancy/diff-so-fancy.svg?style=shield)](https://circleci.com/gh/so-fancy/diff-so-fancy) [![TravisCI build](https://travis-ci.org/so-fancy/diff-so-fancy.svg?branch=master)](https://travis-ci.org/so-fancy/diff-so-fancy) [![AppVeyor build](https://ci.appveyor.com/api/projects/status/github/so-fancy/diff-so-fancy?branch=master&svg=true)](https://ci.appveyor.com/project/stevemao/diff-so-fancy/branch/master)

%package bin
Summary: bin components for the perl-diff-so-fancy package.
Group: Binaries

%description bin
bin components for the perl-diff-so-fancy package.


%prep
%setup -q -n clone_archive
cd %{_builddir}/clone_archive

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594385558
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export FCFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export FFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export CFFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export LDFLAGS="-O3 -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native "
export CXXFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1594385558
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diff-so-fancy
/usr/bin/lib/DiffHighlight.pm
