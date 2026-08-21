file(GLOB IMPL_AC_SOURCE 
	sca_ac_domain_db.cpp
	sca_ac_domain_entity.cpp
	sca_ac_domain_eq.cpp
	sca_ac_domain_globals.cpp
	sca_ac_domain_solver.cpp
	sca_ac_functions.cpp
	sca_ac_noise_start.cpp
	sca_ac_object.cpp
	sca_ac_start.cpp
	)
	
add_library(impl_ac STATIC ${IMPL_AC_SOURCE})
target_include_directories(impl_ac PUBLIC ${SystemCLanguage_INCLUDE_DIRS} ${CMAKE_SOURCE_DIR}/src)

target_link_directories(impl_ac PUBLIC SystemC::systemc)
