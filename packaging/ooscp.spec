Name:           ooscp
Version:        0.1.0
Release:        1%{?dist}
Summary:        Cryptographically validated secure file copy over SSH protocol with bandwidth caps.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooscp
Source0:        ooscp-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooscp is a sovereign, capability-bounded REMOTE COPY written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooscp
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooscp-uninstall

%files
/usr/bin/ooscp
/usr/bin/ooscp-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
