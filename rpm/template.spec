Name:           ros-indigo-geometric-shapes
Version:        0.4.1
Release:        0%{?dist}
Summary:        ROS geometric_shapes package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/geometric_shapes
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       boost-devel
Requires:       console-bridge-devel
Requires:       eigen3-devel
Requires:       qhull-devel
Requires:       ros-indigo-eigen-stl-containers
Requires:       ros-indigo-octomap
Requires:       ros-indigo-random-numbers
Requires:       ros-indigo-resource-retriever
Requires:       ros-indigo-shape-msgs
Requires:       ros-indigo-shape-tools
BuildRequires:  assimp-devel
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  eigen3-devel
BuildRequires:  pkgconfig
BuildRequires:  qhull-devel
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-eigen-stl-containers
BuildRequires:  ros-indigo-octomap
BuildRequires:  ros-indigo-random-numbers
BuildRequires:  ros-indigo-resource-retriever
BuildRequires:  ros-indigo-shape-msgs
BuildRequires:  ros-indigo-shape-tools

%description
This package contains generic definitions of geometric shapes and bodies.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 21 2014 Ioan Sucan <isucan@google.com> - 0.4.1-0
- Autogenerated by Bloom

