# CMake variables such as CMAKE_SOURCE_DIR will be cleared when esp-idf's build system is called. I.e. this file.
# This means that filepaths can't be created from them

include(../cmake/compilerwarnings.cmake)
include(../cmake/clangformat.cmake)
include(../cmake/pch.cmake)

set(SOURCE_FILES src/main.cpp)
set(INCLUDES)
idf_component_register(SRCS ${SOURCE_FILES} INCLUDE_DIRS ${INCLUDES})

set_target_properties(${COMPONENT_LIB} PROPERTIES CXX_STANDARD 23)

use_pch(${COMPONENT_LIB})
apply_compiler_warnings(${COMPONENT_LIB})
enable_clang_format(${COMPONENT_LIB} "../" "/src")

# Enable cppcheck
find_program(PYTHON python)
add_custom_target(${COMPONENT_LIB}_cppcheck_dependency
        COMMAND python cppcheck.py ./main/src
        WORKING_DIRECTORY "../../../"
        COMMENT "Running CppCheck.."
        VERBATIM
)
add_dependencies(${COMPONENT_LIB} ${COMPONENT_LIB}_cppcheck_dependency)
