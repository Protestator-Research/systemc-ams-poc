file(GLOB REPORTING_SOURCE 
	sca_information.cpp)

add_library(reporting STATIC ${REPORTING_SOURCE})

target_link_directories(reporting PUBLIC SystemC::systemc)
target_include_directories(reporting PUBLIC ${SystemCLanguage_INCLUDE_DIRS} ${CMAKE_SOURCE_DIR}/src)