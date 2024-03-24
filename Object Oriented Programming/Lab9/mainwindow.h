#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include "songcontroller.h"
#include <QMainWindow>
#include <QVBoxLayout>
#include <QLabel>
#include <QTextEdit>
#include <QLineEdit>
#include <QFormLayout>
#include <QPushButton>
#include <QHBoxLayout>
#include <QListWidget>
#include <QTableWidget>
#include <QGridLayout>
#include <QObject>
#include <QDebug>
#include <QVector>
#include <QMessageBox>
#include <QShortcut>
#include <QTextEdit>
#include "song.h"
#include "songcontroller.h"
#include "playlist.h"


class Song;

class MainWindow : public QMainWindow

{
    Q_OBJECT

public:
    MainWindow(SongController *ctrl, Playlist *ply, QWidget *parent = nullptr);

    ~MainWindow();

public slots:
    void onAddButton();
    void onDeleteButton();
    void onAddToPlaylistButton();
    void onRemoveFromPlaylistButton();
    void onViewLyricsButton();
    void onSortSongsByTitle();
    void onSortSongsByArtist();
    void onRandomPlaylist();
    void undoAction();
    void redoAction();

private:
    void setupUI();

    //shortcuts

    QShortcut* undoShortcut;
    QShortcut* redoShortcut;

    SongController* m_ctrl;
    Playlist* m_ply;
    QVector<Song*> m_allSongs; //folosesc controller
    QVector<Song*> m_allSongsPlaylist;

    QWidget* m_centralWidget;
    QHBoxLayout* m_mainLayout;
    QVBoxLayout* m_leftVLayout;
    QFormLayout* m_leftFormLayout;
    QHBoxLayout* m_buttonsHLayout;
    QVBoxLayout* m_centerVLayout;
    QFormLayout* m_centerFormLayout;
    QVBoxLayout* m_rightVLayout;
    QFormLayout* m_rightFormLayout;
    QHBoxLayout* m_buttonsHLayout1;
    QFormLayout* m_buttonsFormLayout1;
    QGridLayout* m_buttonsMatrix;
    QGridLayout* m_buttonsMatrix1;
    QGridLayout* m_buttonsMatrixCenter;

    //display the lyrics of a selected song
    QTextEdit* m_displayLyrics;
    QLabel* m_lyricsLable1;

    //display the song sorted by title/artist
    QLabel* m_sortedSongsLable;
    QTextEdit* m_sortedSongs;

    // form layout
    QLabel* m_titleLable;
    QLineEdit* m_titleText;

    QLabel* m_artistLable;
    QLineEdit* m_artistText;

    QLabel* m_yearLable;
    QLineEdit* m_yearText;

    QLabel* m_lyricsLable;
    QLineEdit* m_lyricsText;

    QLabel* m_urlLable;
    QLineEdit* m_urlText;

    QLabel* m_listSongsLabel;
    QListWidget* m_listSongs;

    QLabel* m_playlistLabel;
    QListWidget* m_playlist;

    QLabel* m_noOfSongsPlaylistLabel;
    QLineEdit* m_noOfSongsText;

    // buttons
    QPushButton* m_addButton;
    QPushButton* m_removeButton;
    QPushButton* m_sortTitleButton;
    QPushButton* m_sortArtistButton;
    QPushButton* m_viewLyricsButton;
    QPushButton* m_addToPlaylistButton;
    QPushButton* m_removeFromPlaylistButton;
    QPushButton* m_randomPlaylistButton;

    //display lyrics color background
    QPalette* m_colourBackground;

    QMessageBox* m_messageError;
};
#endif // MAINWINDOW_H
