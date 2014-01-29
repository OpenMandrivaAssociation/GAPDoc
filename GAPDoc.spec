Name:           GAPDoc
Version:        1.5.1
Release:        6%{?dist}
Summary:        GAP documentation tool
# The package is all GPLv2+ except for some of the mathml files
License:        GPLv2+ and MPLv1.1 and W3C
URL:            http://www.math.rwth-aachen.de/~Frank.Luebeck/%{name}/
Source0:        http://www.math.rwth-aachen.de/~Frank.Luebeck/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  gap-devel
Requires:       gap-core
Requires:       texlive
Provides:       gap-pkg-%{name} = %{version}-%{release}

%description
This package describes a document format for writing GAP documentation.

The idea is to define a sufficiently abstract markup language for GAP
documentation which can be (relatively easily) converted into different
output formats.  We used XML to define such a language.

This package provides:
- Utilities to use the documentation which is written in GAPDoc format
  with the GAP help system.  If you don't want to write your own
  (package) documentation you can skip to the last point of this list.
- The description of a markup language for GAP documentation (which is
  defined using the XML standard).
- Three example documents using this language: The GAPDoc documentation
  itself, a short example which demonstrates all constructs defined in
  the GAPDoc language, and a very short example explained in the
  introduction of the main documentation.
- A mechanism for distributing documentation among several files,
  including source code files.
- GAP programs (written by the first named author) which produce from
  documentation written in the GAPDoc language several document formats:
  * text format with color markup for onscreen browsing.
  * LaTeX format and from this PDF- (and DVI)-versions with hyperlinks.
  * HTML (XHTML 1.0 strict) format for reading with a Web-browser (and
    many hooks for CSS layout).
- Utility GAP programs which are used for the above but can be of
  independent interest as well:
  * Unicode strings with translations to and from other encodings
  * further utilities for manipulating strings
  * tools for dealing with BibTeX data
  * another data format BibXMLext for bibliographical data including
    tools to manipulate/translate them
  * a tool ComposedDocument for composing documents which are
    distributed in many files

%prep
%setup -q

# Fix line endings
for fil in mathml/{ctop,mathml,pmathml}.xsl; do
  sed 's/\r//' $fil > $fil.new
  touch -r $fil $fil.new
  mv -f $fil.new $fil
done

%build
# Remove unnecessary documentation clean scripts
rm -f 3k+1/clean doc/clean example/clean

%install
mkdir -p $RPM_BUILD_ROOT%{_gap_dir}/pkg
cd ..
cp -a %{name}-%{version} $RPM_BUILD_ROOT%{_gap_dir}/pkg
rm -f $RPM_BUILD_ROOT%{_gap_dir}/pkg/%{name}-%{version}/{CHANGES,GPL,README}

%posttrans
    %{_bindir}/update-gap-workspace

%postun
    %{_bindir}/update-gap-workspace

%files
%doc CHANGES GPL README
%{_gap_dir}/pkg/%{name}-%{version}/
