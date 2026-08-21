file(GLOB SYNCHRONIZATION_SOURCE 
	sca_sync_value_handle.cpp
	sca_synchronization_alg.cpp
	sca_synchronization_layer_process.cpp
	sca_synchronization_layer.cpp)

add_library(synchronization STATIC ${SYNCHRONIZATION_SOURCE})

target_link_directories(synchronization PUBLIC SystemC::systemc)
target_include_directories(synchronization PUBLIC ${SystemCLanguage_INCLUDE_DIRS} ${CMAKE_SOURCE_DIR}/src)

install_headers(sca_sync_value_handle.h )
