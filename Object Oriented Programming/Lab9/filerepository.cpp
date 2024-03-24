#include "filerepository.h"
#include <stdexcept>
#include <fstream>
#include "song.h"

FileRepository::FileRepository(const string &filepath)
{
    this->filepath = filepath;
}

void FileRepository::load()
{
    std::ifstream in_file(filepath);
    if (!in_file.is_open())
    {
        throw std::runtime_error("Failed to open " + filepath + " file");
    }
    else
    {
        string line, artist, title, lyrics, year, url;
        int ok = 0;

        while (getline(in_file, line))
        {
            title = line;
            getline(in_file, artist);
            getline(in_file, year);
            getline(in_file, lyrics);
            getline(in_file, url);
            Song s = Song(title, artist, std::stoi(year), lyrics, url);
            this->store(s);
        }

    }
    in_file.close();
}

void FileRepository::save()
{
    ofstream out_file(filepath);
    if (!out_file.is_open()) {
        throw std::runtime_error("Failed to save songs in songs_out.txt");
    }
    else
    {
        for (const auto& song : getAll())
        {
            out_file<<song.getTitle()<< "\n"<<song.getArtist()<<"\n"<<song.getYear()<<"\n";
            std::vector<std::string> lyrics = song.getLyrics();
            for(int i = 0; i < lyrics.size(); i++)
            {
                out_file<<lyrics.at(i)<<" ";
            }
            out_file<<"\n";
            out_file<<song.getUrl();
            out_file<<"\n";
        }

    }
    out_file.close();
}

void FileRepository::store(const Song &s)
{
    Repository::store(s);
    save();
}

void FileRepository::remove(const Song &s)
{
    Repository::remove(s);
    save();
}



