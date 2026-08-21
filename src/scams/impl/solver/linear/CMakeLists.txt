file(GLOB LINEAR_SOURCE
	sca_linear_solver.cpp)

add_library(linear STATIC ${LINEAR_SOURCE})

target_link_directories(linear PUBLIC SystemC::systemc)
target_include_directories(linear PUBLIC ${SystemCLanguage_INCLUDE_DIRS} ${CMAKE_SOURCE_DIR}/src)

install_headers(
	sca_linear_solver_parameters.h)