# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.2

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# Produce verbose output by default.
VERBOSE = 1

# The CMake executable.
CMAKE_COMMAND = /home/juju/VTK5.0/Cmake/bin/cmake

# The command to remove a file.
RM = /home/juju/VTK5.0/Cmake/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /home/juju/VTK5.0/Cmake/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/juju/VTK5.0/VTK

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/juju/VTK5.0/VTK

# Include any dependencies generated for this target.
include Wrapping/Tcl/CMakeFiles/vtk.dir/depend.make

# Include the compile flags for this target's objects.
include Wrapping/Tcl/CMakeFiles/vtk.dir/flags.make

Wrapping/Tcl/CMakeFiles/vtk.dir/depend.make.mark: Wrapping/Tcl/vtkTkAppInit.cxx

Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o: Wrapping/Tcl/vtkTkAppInit.cxx
	@echo "Building CXX object Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o"
	c++  $(CXX_FLAGS) -o Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o -c /home/juju/VTK5.0/VTK/Wrapping/Tcl/vtkTkAppInit.cxx

Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o.requires:

Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o.provides: Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o.requires
	$(MAKE) -f Wrapping/Tcl/CMakeFiles/vtk.dir/build.make Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o.provides.build

Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o.provides.build: Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o

Wrapping/Tcl/CMakeFiles/vtk.dir/depend: Wrapping/Tcl/CMakeFiles/vtk.dir/depend.make.mark

Wrapping/Tcl/CMakeFiles/vtk.dir/depend.make.mark:
	@echo "Scanning dependencies of target vtk"
	$(CMAKE_COMMAND) -E cmake_depends  "Unix Makefiles" /home/juju/VTK5.0/VTK /home/juju/VTK5.0/VTK/Wrapping/Tcl /home/juju/VTK5.0/VTK/Wrapping/Tcl/CMakeFiles/vtk.dir/DependInfo.cmake

# Object files for target vtk
vtk_OBJECTS = \
"CMakeFiles/vtk.dir/vtkTkAppInit.o"

# External object files for target vtk
vtk_EXTERNAL_OBJECTS =

bin/vtk: Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o
bin/vtk: bin/libvtkCommonTCL.so
bin/vtk: bin/libvtkFilteringTCL.so
bin/vtk: bin/libvtkGraphicsTCL.so
bin/vtk: bin/libvtkImagingTCL.so
bin/vtk: bin/libvtkIOTCL.so
bin/vtk: bin/libvtkRenderingTCL.so
bin/vtk: bin/libvtkVolumeRenderingTCL.so
bin/vtk: bin/libvtkHybridTCL.so
bin/vtk: bin/libvtkWidgetsTCL.so
bin/vtk: bin/libvtkParallelTCL.so
bin/vtk: bin/libvtkVolumeRendering.so
bin/vtk: bin/libvtkWidgets.so
bin/vtk: bin/libvtkHybrid.so
bin/vtk: bin/libvtkParallel.so
bin/vtk: bin/libvtkexoIIc.so
bin/vtk: bin/libvtkNetCDF.so
bin/vtk: bin/libvtkRendering.so
bin/vtk: bin/libvtkftgl.so
bin/vtk: bin/libvtkfreetype.so
bin/vtk: /usr/lib/libGL.so
bin/vtk: /usr/X11R6/lib/libX11.so
bin/vtk: /usr/X11R6/lib/libXext.so
bin/vtk: bin/libvtkGraphics.so
bin/vtk: bin/libvtkImaging.so
bin/vtk: /usr/lib/libtk8.4.so
bin/vtk: bin/libvtkIO.so
bin/vtk: bin/libvtkDICOMParser.so
bin/vtk: bin/libvtkpng.so
bin/vtk: bin/libvtktiff.so
bin/vtk: bin/libvtkzlib.so
bin/vtk: bin/libvtkjpeg.so
bin/vtk: bin/libvtkexpat.so
bin/vtk: bin/libvtkMPEG2Encode.so
bin/vtk: bin/libvtkFiltering.so
bin/vtk: bin/libvtkCommon.so
bin/vtk: bin/libvtksys.so
bin/vtk: /usr/lib/libtcl8.4.so
	@echo "Linking CXX executable ../../bin/vtk"
	$(CMAKE_COMMAND) -E remove -f ../../bin/vtk
	cd /home/juju/VTK5.0/VTK/Wrapping/Tcl && c++    -Wno-deprecated  -fPIC   $(vtk_OBJECTS) $(vtk_EXTERNAL_OBJECTS)  -o ../../bin/vtk -rdynamic -L/home/juju/VTK5.0/VTK/bin -L/usr/X11R6/lib -lvtkCommonTCL -lvtkFilteringTCL -lvtkGraphicsTCL -lvtkImagingTCL -lvtkIOTCL -lvtkRenderingTCL -lvtkVolumeRenderingTCL -lvtkHybridTCL -lvtkWidgetsTCL -lvtkParallelTCL -lvtkVolumeRendering -lvtkWidgets -lvtkHybridTCL -lvtkHybrid -lvtkParallel -lvtkexoIIc -lvtkNetCDF -lvtkRenderingTCL -lvtkRendering -lvtkftgl -lvtkfreetype -lGL -lXt -lSM -lICE -lSM -lICE -lSM -lICE -lX11 -lXext -lX11 -lXext -lX11 -lXext -lvtkGraphicsTCL -lvtkGraphics -lvtkImagingTCL -lvtkImaging -ltk8.4 -lvtkIOTCL -lvtkIO -lvtkDICOMParser -lvtkpng -lvtktiff -lvtkzlib -lvtkjpeg -lvtkexpat -lvtkMPEG2Encode -lvtkFilteringTCL -lvtkFiltering -lvtkCommonTCL -lvtkCommon -lvtksys -lpthread -ldl -lm -ltcl8.4 -lm 

# Convenience name for target.
Wrapping/Tcl/CMakeFiles/vtk.dir/build: bin/vtk

Wrapping/Tcl/CMakeFiles/vtk.dir/requires: Wrapping/Tcl/CMakeFiles/vtk.dir/vtkTkAppInit.o.requires

Wrapping/Tcl/CMakeFiles/vtk.dir/clean:
	cd /home/juju/VTK5.0/VTK/Wrapping/Tcl && $(CMAKE_COMMAND) -E remove -f ../../bin/vtk $(vtk_OBJECTS)
