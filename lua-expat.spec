%define _disable_ld_no_undefined 1

%define lua_version %(lua -e 'print(_VERSION)' | cut -d ' ' -f 2)
%define lua_libdir %{_libdir}/lua/%{lua_version}
%define lua_pkgdir %{_datadir}/lua/%{lua_version}

Name:           lua-expat
Version:        1.5.2
Release:        1
Summary:        SAX XML parser based on the Expat library
Group:          Development/Other
License:        MIT
URL:            https://lunarmodules.github.io/luaexpat/
Source0:        https://github.com/lunarmodules/luaexpat/archive/%{version}/luaexpat-%{version}.tar.gz

Requires:       lua

BuildRequires:  make
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  expat-devel >= 2.4.0

%description
LuaExpat is a SAX XML parser based on the Expat library.

%prep
%setup -q -n luaexpat-%{version}

%build
%make_build \
  CFLAGS="$RPM_OPT_FLAGS -fPIC -std=c99" LDFLAGS="$RPM_LD_FLAGS" \
  LUA_V=%{lua_version} \
  LUA_CDIR=%{lua_libdir} LUA_LDIR=%{lua_pkgdir} \
  LUA_INC=-I%{_includedir}


%install
%make_install LUA_CDIR=%{lua_libdir} LUA_LDIR=%{lua_pkgdir}


%check
lua -e \
  'package.cpath="%{buildroot}%{lua_libdir}/?.so;"..package.cpath;
   package.path="%{buildroot}%{lua_pkgdir}/?.lua;"..package.path;
   local lxp = require("lxp"); print("Hello from "..lxp._VERSION.."!");'


%files
%license LICENSE
%doc README.md docs/*
%{lua_libdir}/lxp.so
%{lua_pkgdir}/lxp/
