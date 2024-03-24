cmake_minimum_required(VERSION 3.24)
project(untitled76)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH /Users/local.user/Qt/6.5.0/macos/lib/cmake)

find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(untitled76 main.cpp filerepository.cpp
        filerepository.h
        main.cpp
        mainwindow.cpp
        mainwindow.h
        repository.cpp
        repository.h
        song.cpp
        song.h
        songcontroller.cpp
        songcontroller.h
        songexception.cpp
        songexception.h action.cpp add.cpp delete.cpp filerepositorytest.cpp playlist.cpp repositorytest.cpp songcontrollertest.cpp)

target_link_libraries(untitled76
        Qt::Core
        Qt::Gui
        Qt::Widgets
        )
