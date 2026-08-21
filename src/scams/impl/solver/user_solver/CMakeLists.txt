file(GLOB USER_SOLVER_SOURCE 
	sca_generic_user_solver.cpp)

add_library(user_solver STATIC ${USER_SOLVER_SOURCE})

target_link_directories(user_solver PUBLIC SystemC::systemc core)
target_include_directories(user_solver PUBLIC ${SystemCLanguage_INCLUDE_DIRS} ${CMAKE_SOURCE_DIR}/src)

set_target_properties(user_solver PROPERTIES LINKER_LANGUAGE CXX )