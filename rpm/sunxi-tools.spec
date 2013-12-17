# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       sunxi-tools

# >> macros
# << macros

Summary:    Allwinner A10 Hacking Tools
Version:    1.1
Release:    1
Group:      Development/Tools
License:    GPLv2
URL:        http://linux-sunxi.org
Source0:    %{name}-%{version}.tar.bz2
Source100:  sunxi-tools.yaml
BuildRequires:  pkgconfig(libusb-1.0)

%description
Tools to help hacking Allwinner A10 (aka sun4i) based devices and possibly
it's successors, that's why the 'x' in the package name.



%prep
%setup -q -n %{name}-%{version}/sunxi-tools

# >> setup
# << setup

%build
# >> build pre
make all
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
mkdir -p %{buildroot}/%{_bindir}/
cp -a fel bin/fel-pio.bin nand-part fel-gpio %{buildroot}/%{_bindir}
cp -a adb-devprobe.sh bootinfo fexc pio bin2fex fex2bin %{buildroot}/%{_bindir}
# << install post


%files
%defattr(-,root,root,-)
%{_bindir}/*
# >> files
# << files
