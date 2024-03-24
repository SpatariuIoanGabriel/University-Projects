#include "mainwindow.h"
#include "ui_mainwindow.h"
#include"songexception.h"
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QTableWidget>
#include <QKeySequence>
#include <QFormLayout>
#include <QHBoxLayout>


MainWindow::MainWindow(SongController *ctrl, Playlist *ply, QWidget *parent)
    : QMainWindow(parent)
{
    this->setupUI();
    this->m_ctrl = ctrl;
    this->m_ply = ply;

}

MainWindow::~MainWindow()
{
    delete m_mainLayout;
    delete m_leftVLayout;
    delete m_buttonsMatrix;
    delete m_centerVLayout;
    delete m_rightVLayout;
    delete m_buttonsHLayout1;
    delete m_centralWidget;
}

void MainWindow::onAddButton()
{
    QString title = m_titleText->displayText();
    QString artist = m_artistText->displayText();
    QString year = m_yearText->displayText();
    QString lyrics = m_lyricsText->displayText();
    QString url = m_urlText->displayText();

    try{
        Song *s = new Song(title.toStdString(), artist.toStdString(), year.toInt(), lyrics.toStdString(), url.toStdString());
        m_allSongs.push_back(s);

        m_listSongs->addItem(QString::fromStdString(s->toString()));

        m_ctrl->add(title.toStdString(), artist.toStdString(), year.toInt(), lyrics.toStdString(), url.toStdString());
    }
    catch (const std::invalid_argument& expt)

    {
        QMessageBox::information(this, "Message", "Error", QMessageBox::Ok);

    }
    m_titleText->clear();
    m_artistText->clear();
    m_yearText->clear();
    m_lyricsText->clear();
    m_urlText->clear();
}

void MainWindow::onDeleteButton()
{
    QListWidgetItem* item = m_listSongs->currentItem();
    int row = m_listSongs->currentRow();
    Song s = m_ctrl->getRepository().getAll()[row];
    m_ctrl->remove(s);
    if(item != nullptr)
    {
        m_allSongs.remove(m_listSongs->row(item));
        delete m_listSongs->takeItem(m_listSongs->row(item));
    }
}

void MainWindow::onAddToPlaylistButton()
{
    QListWidgetItem* item = m_listSongs->currentItem();
    if(item != nullptr)
    {
        m_allSongsPlaylist.append(m_allSongs.at(m_listSongs->row(item)));
        m_playlist->addItem(item->text());
    }
}

void MainWindow::onRemoveFromPlaylistButton()
{
    QListWidgetItem* item = m_playlist->currentItem();
    if(item != nullptr)
    {
        delete m_playlist->takeItem(m_playlist->row(item));
    }
}

void MainWindow::onViewLyricsButton()
{
    int row = m_listSongs->currentRow();
    vector<Song> songs = m_ctrl->getRepository().getAll();
    std::vector<std::string> lyrics = songs[row].getLyrics();
    QString qLyrics;
    for (const std::string& line : lyrics)
    {
        qLyrics += QString::fromStdString(line) + "\n";
    }
    m_displayLyrics->setPlainText(qLyrics);

}

int currentSortCriterionTitles = 0;

void MainWindow::onSortSongsByTitle()
{
    switch (currentSortCriterionTitles) {
    case 0:
    {
        vector<Song> songs = m_ctrl->sortByTitles(true);

        QString qLyrics;
        for(int i = 0; i < songs.size(); i++)

            qLyrics += QString::fromStdString(songs[i].getTitle()) + "\n";

        m_sortedSongs->setPlainText(qLyrics);
        break;
    }

    case 1:
    {
        vector<Song> songs1 = m_ctrl->sortByTitles(false);

        QString qLyrics1;
        for(int i = 0; i < songs1.size(); i++)
            qLyrics1 += QString::fromStdString(songs1[i].getTitle()) + "\n";

        m_sortedSongs->setPlainText(qLyrics1);
        break;
    }
    default:
        break;
    }
    currentSortCriterionTitles = (currentSortCriterionTitles + 1) % 2;

}

int currentSortCriterionArtist = 0;

void MainWindow::onSortSongsByArtist()
{
    switch (currentSortCriterionArtist) {
    case 0:
    {
        vector<Song> songs = m_ctrl->sortByArtistName(true);

        QString qLyrics;
        for(int i = 0; i < songs.size(); i++)

            qLyrics += QString::fromStdString(songs[i].getArtist()) + "\n";

        m_sortedSongs->setPlainText(qLyrics);
        break;
    }

    case 1:
    {
        vector<Song> songs1 = m_ctrl->sortByArtistName(false);

        QString qLyrics1;
        for(int i = 0; i < songs1.size(); i++)
            qLyrics1 += QString::fromStdString(songs1[i].getArtist()) + "\n";

        m_sortedSongs->setPlainText(qLyrics1);
        break;
    }
    default:
        break;
    }
    currentSortCriterionArtist = (currentSortCriterionArtist + 1) % 2;
}

void MainWindow::onRandomPlaylist()
{
    m_playlist->clear();
    QString number = m_noOfSongsText->displayText();
    vector<Song> songs1 = m_ply->generateRandom(number.toInt(), m_ctrl->getRepository().getAll());
    for(int i = 0; i < songs1.size(); i++)
    {
        QString title = QString::fromStdString(songs1[i].getTitle());
        QString artist = QString::fromStdString(songs1[i].getArtist());
        QString itemText = title + " by " + artist;
        QListWidgetItem* item = new QListWidgetItem(itemText);
        m_playlist->addItem(item);

    }

}




void MainWindow::undoAction()
{
    m_ctrl->undo();
}

void MainWindow::redoAction()
{
    m_ctrl->redo();
}

void MainWindow::setupUI()

{
    undoShortcut = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_Z), this);
    redoShortcut = new QShortcut(QKeySequence(Qt::CTRL + Qt::Key_Y), this);

    m_messageError = new QMessageBox();

    m_centralWidget = new QWidget();
    m_mainLayout = new QHBoxLayout();
    m_leftVLayout = new QVBoxLayout();
    m_buttonsHLayout = new QHBoxLayout();
    m_buttonsMatrix = new QGridLayout();
    m_buttonsMatrix1 = new QGridLayout();
    m_buttonsMatrixCenter = new QGridLayout();

    m_displayLyrics = new QTextEdit;
    m_displayLyrics->setReadOnly(true);
    m_colourBackground = new QPalette;
    m_colourBackground->setColor(QPalette::Base, Qt::darkGray);
    m_colourBackground->setColor(QPalette::Text, Qt::white);
    m_displayLyrics->setPalette(*m_colourBackground);
    m_lyricsLable1 = new QLabel("Lyrics:");

    m_sortedSongs = new QTextEdit;
    m_sortedSongs->setReadOnly(true);
    m_sortedSongs->setPalette(*m_colourBackground);
    m_sortedSongsLable = new QLabel("Sorted songs: ");


    m_listSongsLabel = new QLabel("All songs:");
    m_listSongs = new QListWidget();
    m_leftFormLayout = new QFormLayout();

    m_titleLable = new QLabel("Title:");
    m_titleText = new QLineEdit();

    m_artistLable = new QLabel("Artist:");
    m_artistText = new QLineEdit();

    m_yearLable = new QLabel("Year:");
    m_yearText = new QLineEdit();

    m_lyricsLable = new QLabel("Lyrics:");
    m_lyricsText = new QLineEdit();

    m_urlLable = new QLabel("URL:");
    m_urlText = new QLineEdit();

    m_playlistLabel = new QLabel("Playlist:");
    m_playlist = new QListWidget();

    m_noOfSongsPlaylistLabel = new QLabel("No of songs: ");
    m_noOfSongsText = new QLineEdit();

    m_leftFormLayout->addRow(m_titleLable, m_titleText);
    m_leftFormLayout->addRow(m_artistLable, m_artistText);
    m_leftFormLayout->addRow(m_yearLable, m_yearText);
    m_leftFormLayout->addRow(m_lyricsLable, m_lyricsText);
    m_leftFormLayout->addRow(m_urlLable, m_urlText);
    m_leftVLayout->addWidget(m_listSongsLabel);
    m_leftVLayout->addWidget(m_listSongs);


    m_addButton = new QPushButton("Add");
    m_removeButton = new QPushButton("Remove");
    m_sortTitleButton = new QPushButton("Sort by title");
    m_sortArtistButton = new QPushButton("Sort by artist");
    m_addToPlaylistButton = new QPushButton("Add to playlist");
    m_removeFromPlaylistButton = new QPushButton("Remove from playlist");
    m_randomPlaylistButton = new QPushButton("Random playlist");
    m_viewLyricsButton = new QPushButton("View lyrics");

    m_leftVLayout->addLayout(m_leftFormLayout);
    m_leftVLayout->addLayout(m_buttonsMatrix);

    m_buttonsMatrix->addWidget(m_addButton, 0, 0);
    m_buttonsMatrix->addWidget(m_removeButton, 0, 1);
    m_buttonsMatrix->addWidget(m_sortArtistButton, 1, 0);
    m_buttonsMatrix->addWidget(m_sortTitleButton, 1, 1);


    m_centerVLayout = new QVBoxLayout();
    m_centerFormLayout = new QFormLayout();
    m_centerVLayout->addLayout(m_buttonsMatrixCenter);
    m_buttonsMatrixCenter->addWidget(m_addToPlaylistButton, 0, 0);
    m_buttonsMatrixCenter->addWidget(m_removeFromPlaylistButton, 1, 0);
    m_buttonsMatrixCenter->addWidget(m_viewLyricsButton, 2, 0);
    m_buttonsMatrixCenter->addWidget(m_lyricsLable1, 3, 0);
    m_buttonsMatrixCenter->addWidget(m_displayLyrics, 4, 0);
    m_buttonsMatrixCenter->addWidget(m_sortedSongsLable, 5, 0);
    m_buttonsMatrixCenter->addWidget(m_sortedSongs, 6, 0);

    m_rightVLayout = new QVBoxLayout();
    m_rightFormLayout = new QFormLayout();

    m_rightFormLayout->addWidget(m_playlistLabel);
    m_rightFormLayout->addWidget(m_playlist);


    m_rightVLayout->addLayout(m_rightFormLayout);

    m_buttonsHLayout1 = new QHBoxLayout();

    m_buttonsMatrix1->addWidget(m_randomPlaylistButton, 0, 0);
    m_buttonsMatrix1->addWidget(m_noOfSongsPlaylistLabel, 1, 0);
    m_buttonsMatrix1->addWidget(m_noOfSongsText, 2, 0);


    m_rightVLayout->addLayout(m_buttonsMatrix1);

    m_rightVLayout->addLayout(m_buttonsHLayout1);

    m_mainLayout->addLayout(m_leftVLayout);
    m_mainLayout->addLayout(m_centerVLayout);
    m_mainLayout->addLayout(m_rightVLayout);
    m_centralWidget->setLayout(m_mainLayout);
    this->setCentralWidget(m_centralWidget);

    QObject::connect(m_addButton, &QPushButton::clicked, this, &MainWindow::onAddButton);
    QObject::connect(m_removeButton, &QPushButton::clicked, this, &MainWindow::onDeleteButton);
    QObject::connect(m_addToPlaylistButton, &QPushButton::clicked, this, &MainWindow::onAddToPlaylistButton);
    QObject::connect(m_removeFromPlaylistButton, &QPushButton::clicked, this, &MainWindow::onRemoveFromPlaylistButton);
    QObject::connect(m_viewLyricsButton, &QPushButton::clicked, this, &MainWindow::onViewLyricsButton);
    QObject::connect(m_sortTitleButton, &QPushButton::clicked, this, &MainWindow::onSortSongsByTitle);
    QObject::connect(m_sortArtistButton, &QPushButton::clicked, this, &MainWindow::onSortSongsByArtist);
    QObject::connect(m_randomPlaylistButton, &QPushButton::clicked, this, &MainWindow::onRandomPlaylist);
    QObject::connect(undoShortcut, &QShortcut::activated, this, &MainWindow::undoAction);
    QObject::connect(redoShortcut, &QShortcut::activated, this, &MainWindow::redoAction);

}
