%global module keras-applications
%global mod %(m=%{module}; echo ${m:0:1})

Summary:	Applications module of the Keras deep learning library
Name:		python-%{module}
Version:	1.0.8
Release:	2
Source0:	https://github.com/keras-team/%{module}/archive/refs/tags/%{version}/%{module}-%{version}.tar.gz
#Source0:	https://pypi.io/packages/source/%{mod}/%{module}/%{module}-%{version}.tar.gz
License:	Expat
Group:		Development/Python
Url:		https://keras.io/
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(python-distutils-extra)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(setuptools)

BuildArch:	noarch

%description
Keras is a deep learning API written in Python, running on top of the
machine learning platform TensorFlow. It was developed with a focus on
enabling fast experimentation. Being able to go from idea to result as
fast as possible is key to doing good research.

Keras is:
  - Simple   -- but not simplistic. Keras reduces developer cognitive
                load to free you to focus on the parts of the problem
                that really matter.
  - Flexible -- Keras adopts the principle of progressive disclosure
                of complexity: simple workflows should be quick and
                easy, while arbitrarily advanced workflows should be
                possible via a clear path that builds upon what you've
                already learned.
  - Powerful -- Keras provides industry-strength performance and
                scalability: it is used by organizations and companies
                including NASA, YouTube, or Waymo.

Keras Applications is the applications module of the Keras deep learning
library. It provides model definitions and pre-trained weights for a
number of popular archictures, such as VGG16, ResNet50, Xception,
MobileNet, and more.

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{py3_puresitedir}/keras_applications
%{py3_puresitedir}/*.egg-info/

#-----------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py3_build

%install
%py3_install
