QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    action.cpp \
    actionadd.cpp \
    actiondelete.cpp \
    filerepository.cpp \
    filerepositorytest.cpp \
    main.cpp \
    mainwindow.cpp \
    playlist.cpp \
    repository.cpp \
    repositorytest.cpp \
    song.cpp \
    songcontroller.cpp \
    songcontrollertest.cpp \
    songexception.cpp

HEADERS += \
    action.h \
    actionadd.h \
    actiondelete.h \
    filerepository.h \
    filerepositorytest.h \
    mainwindow.h \
    playlist.h \
    repository.h \
    repositorytest.h \
    song.h \
    songcontroller.h \
    songcontrollertest.h \
    songexception.h

FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    ../Library/Mobile Documents/com~apple~TextEdit/Documents/song1.rtf \
    ../Library/Mobile Documents/com~apple~TextEdit/Documents/song1.rtf \
    songs.txt
