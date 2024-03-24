#include "song.h"
#include<string>
#include<sstream>
#include<cctype>
#include<algorithm>

Song::Song(): title{""}, artist{""}, year{0}, lyrics{""}, url{""}
{}

Song::Song(string title, string artist, int year, string lyrics, string url)
{
    this->artist = artist;
    this->title = title;
    this->year = year;

    std::replace_if(lyrics.begin(), lyrics.end(), [](char c) {return std::ispunct(c);}, ' ');
    stringstream ss(lyrics);
    string word;
    while (getline(ss, word, ' '))
    {
        for (int i = 0; i < word.size(); i++)
        {
            word[i] = tolower(word[i]);
        }
        this->lyrics.push_back(word);
    }
    this->url = url;


}

string Song::getTitle() const
{
    return title;
}

void Song::setTitle(const string &newTitle)
{
    title = newTitle;
}

string Song::getArtist() const
{
    return artist;
}

void Song::setArtist(const string &newArtist)
{
    artist = newArtist;
}

int Song::getYear() const
{
    return year;
}

void Song::setYear(int newYear)
{
    year = newYear;
}

std::vector<string> Song::getLyrics() const
{
    return lyrics;
}

void Song::setLyrics(const std::vector<string> &newLyrics)
{
    lyrics = newLyrics;
}

string Song::getUrl() const
{
    return url;
}

void Song::setUrl(const string &newUrl)
{
    url = newUrl;
}

string Song::toString()
{
    string result = "";
    ostringstream ss;
    ss<<year;
    result = result + title + " by " + artist + " " + to_string(year) + " ";
    for (int i = 0; i < lyrics.size(); i++)
    {
        result = result + lyrics[i] + " ";
    }
    result = result + url + " ";
    return result;
}

bool Song::operator<(const Song &other) const
{
    return title < other.title;

}
