#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

// Abstract base class
template <typename T>
class Classifier {
public:
    virtual void fit(T trainImages, vector<int> trainLabels) = 0; // train
    virtual vector<int> predict(T) = 0; // predicted labels
    virtual bool save(string filepath) = 0; // save model to a file
    virtual bool load(string filepath) = 0; // load model from a file
    virtual double eval(T, vector<int> trainLabels) = 0; // evaluate accuracy(correct predictions)
};

// KNNClassifier subclass
class KNNClassifier : public Classifier<vector<vector<int>>> {
private:
    vector<vector<int>> trainImages;
    vector<int> trainLabels;

public:
    void fit(vector<vector<int>> trainImages, vector<int> trainLabels) {
        this->trainImages = trainImages;
        this->trainLabels = trainLabels;
    }

    vector<int> predict(vector<vector<int>> testImages) {
        vector<int> predictedLabels;
        for (const auto& image : testImages) {
            int nearestNeighbor = findNearestNeighbor(image);
            predictedLabels.push_back(trainLabels[nearestNeighbor]);
        }
        return predictedLabels;
    }

    bool save(string filepath) {
        ofstream file(filepath);
        if (!file.is_open()) {
            return false;
        }

        // Save trainImages
        for (const auto& image : trainImages) {
            for (const auto& pixel : image) {
                file << pixel << ",";
            }
            file << "\n";
        }

        // Save trainLabels
        for (const auto& label : trainLabels) {
            file << label << "\n";
        }

        file.close();
        return true;
    }

    bool load(string filepath) {
        vector<vector<int>> trainImages;
        vector<int> trainLabels;

        ifstream file(filepath);
        if (file.is_open()) {
            string line;
            while (getline(file, line)) {
                // Extract the label from the beginning of the line
                size_t pos = line.find(',');
                int label = stoi(line.substr(0, pos));

                // Parse the image data
                vector<int> image;
                line.erase(0, pos + 1);
                while ((pos = line.find(',')) != string::npos) {
                    string token = line.substr(0, pos);
                    image.push_back(stoi(token));
                    line.erase(0, pos + 1);
                }

                trainImages.push_back(image);
                trainLabels.push_back(label);
            }

            file.close();
        }
        else {
            cout << "Failed to open file." << endl;
            return true;
        }
        return false;
    }

    double eval(vector<vector<int>> testImages, vector<int> trainLabels) {
        vector<int> predictedLabels = predict(testImages);
        int correctPredictions = 0;
        for (int i = 0; i < predictedLabels.size(); ++i) {
            if (predictedLabels[i] == trainLabels[i]) {
                correctPredictions++;
            }
        }
        return static_cast<double>(correctPredictions) / predictedLabels.size();
    }

private:
    // Find the nearest neighbor to a test image
    int findNearestNeighbor(const vector<int>& testImage) {
        int minDistance = INT_MAX;
        int nearestNeighbor = 0;

        for (int i = 0; i < trainImages.size(); ++i) {
            int distance = calculateDistance(testImage, trainImages[i]);
            if (distance < minDistance) {
                minDistance = distance;
                nearestNeighbor = i;
            }
        }

        return nearestNeighbor;
    }

    // Calculate the Euclidean distance between two images
    int calculateDistance(const vector<int>& image1, const vector<int>& image2) {
        int distance = 0;

        for (int i = 0; i < image1.size(); ++i) {
            distance += pow(image1[i] - image2[i], 2);
        }

        return distance;
    }
};

// BayesClassifier subclass
class BayesClassifier : public Classifier<vector<vector<int>>> {
private:
    vector<double> prior; // Prior probabilities
    vector<vector<double>> likelihood; // Likelihood probabilities

public:
    void fit(vector<vector<int>> trainImages, vector<int> trainLabels) {
        // Calculate prior probabilities
        int numInstances = trainImages.size();
        int numClasses = *max_element(trainLabels.begin(), trainLabels.end()) + 1;
        prior.resize(numClasses, 0.0);

        for (int label : trainLabels) {
            prior[label]++;
        }

        for (double& p : prior) {
            p /= numInstances;
        }

        // Calculate likelihood probabilities
        int numFeatures = trainImages[0].size();
        likelihood.resize(numClasses, vector<double>(numFeatures, 0.0));
        vector<int> classCounts(numClasses, 0);

        for (int i = 0; i < numInstances; ++i) {
            int label = trainLabels[i];
            classCounts[label]++;

            for (int j = 0; j < numFeatures; ++j) {
                if (trainImages[i][j] == 255) {
                    likelihood[label][j]++;
                }
            }
        }

        for (int i = 0; i < numClasses; ++i) {
            for (int j = 0; j < numFeatures; ++j) {
                likelihood[i][j] = (likelihood[i][j] + 1.0) / (classCounts[i] + 2.0);
            }
        }
    }

    vector<int> predict(vector<vector<int>> testImages) {
        vector<int> predictions;

        for (const auto& image : testImages) {
            vector<double> logPosteriors(prior.size(), 0.0);

            for (int i = 0; i < prior.size(); ++i) {
                logPosteriors[i] = log(prior[i]);

                for (int j = 0; j < image.size(); ++j) {
                    if (image[j] == 255) {
                        logPosteriors[i] += log(likelihood[i][j]);
                    }
                    else {
                        logPosteriors[i] += log(1.0 - likelihood[i][j]);
                    }
                }
            }

            int predictedLabel = distance(logPosteriors.begin(), max_element(logPosteriors.begin(), logPosteriors.end()));
            predictions.push_back(predictedLabel);
        }

        return predictions;
    }

    bool save(string filepath) {
        ofstream file(filepath);
        if (!file.is_open()) {
            return false;
        }

        // Save prior probabilities
        for (const auto& p : prior) {
            file << p << ",";
        }
        file << "\n";

        // Save likelihood probabilities
        for (const auto& classLikelihoods : likelihood) {
            for (const auto& likelihoodValue : classLikelihoods) {
                file << likelihoodValue << ",";
            }
            file << "\n";
        }

        file.close();
        return true;
    }

    bool load(string filepath) {
        ifstream file(filepath);
        if (file.is_open()) {
            // Load prior probabilities
            string line;
            if (getline(file, line)) {
                size_t pos = 0;
                string token;
                while ((pos = line.find(',')) != string::npos) {
                    token = line.substr(0, pos);
                    prior.push_back(stod(token));
                    line.erase(0, pos + 1);
                }
            }

            // Load likelihood probabilities
            while (getline(file, line)) {
                size_t pos = 0;
                string token;
                vector<double> classLikelihoods;
                while ((pos = line.find(',')) != string::npos) {
                    token = line.substr(0, pos);
                    classLikelihoods.push_back(stod(token));
                    line.erase(0, pos + 1);
                }
                likelihood.push_back(classLikelihoods);
            }

            file.close();
            return true;
        }
        else {
            cout << "Failed to open file." << endl;
            return false;
        }
    }

    double eval(vector<vector<int>> testImages, vector<int> trainLabels) {
        vector<int> predictedLabels = predict(testImages);
        int correctPredictions = 0;
        for (int i = 0; i < predictedLabels.size(); ++i) {
            if (predictedLabels[i] == trainLabels[i]) {
                correctPredictions++;
            }
        }
        //converts the correctPredictions variable from its original type to a double type.
        return static_cast<double>(correctPredictions) / predictedLabels.size();
    }
};

int main() {
    // Read MNIST dataset from CSV file
    vector<vector<int>> trainImages;
    vector<int> trainLabels;

    ifstream file("mnist_train.csv");
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            // Extract the label from the beginning of the line
            size_t pos = line.find(',');
            int label = stoi(line.substr(0, pos)); // string to int

            // Parse the image data
            vector<int> image;
            line.erase(0, pos + 1);
            while ((pos = line.find(',')) != string::npos) {
                string token = line.substr(0, pos);
                image.push_back(stoi(token));
                line.erase(0, pos + 1);
            }

            trainImages.push_back(image);
            trainLabels.push_back(label);
        }

        file.close();
    }
    else {
        cout << "Failed to open file." << endl;
        return 1;
    }

    vector<vector<int>> Images = trainImages;
    vector<int> Labels = trainLabels;



    cout << "Size of trainImages: " << trainImages.size() << endl;
    cout << "Size of Images:" << Images.size() << endl;

    if (!Images.empty()) {
        const vector<int>& firstImage = Images[0];
        for (int pixelValue : firstImage) {
            cout << pixelValue << " ";
        }
        cout << endl;
        cout << endl;
        const vector<int>& secondImage = Images[1];
        for (int pixelValue : secondImage) {
            cout << pixelValue << " ";
        }
        cout << endl;
    }
    cout <<endl<< "FIRST 10 LABELS:" << endl;
    for (int i = 0; i < 10 && i < trainLabels.size(); ++i) {
        cout << trainLabels[i] << endl;
    }


    //BAYES TRAINING
    BayesClassifier bayes;
    bayes.fit(trainImages, trainLabels);
    vector<int> bayesPredictions = bayes.predict(trainImages);
    double bayesAccuracy = bayes.eval(trainImages, trainLabels);
    cout << "The accuracy of the bayesPredictions is:" << bayesAccuracy << endl;

    return 0;
}