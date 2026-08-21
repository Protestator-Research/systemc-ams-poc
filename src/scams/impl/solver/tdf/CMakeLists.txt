file(GLOB SOLVERTDF_SOURCE 
	sca_tdf_solver.cpp)

add_library(solvertdf STATIC ${SOLVERTDF_SOURCE})

target_link_directories(solvertdf PUBLIC SystemC::systemc)

target_include_directories(solvertdf PUBLIC ${SystemCLanguage_INCLUDE_DIRS} ${CMAKE_SOURCE_DIR}/src)