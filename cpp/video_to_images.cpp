#include<opencv2/opencv.hpp>
#include<iostream>
#include <ctime>
#include <chrono>

// Namespace to nullify use of cv::function(); syntax
using namespace std;
using namespace cv;

int main()
{
    // Replace path_to_file with the path to video file
	VideoCapture vid_capture(path_to_file);

    // 3 CAP_PROP_FRAME_WIDTH 4- CAP_PROP_FRAME_HEIGHT

	int frame_width = static_cast<int>(vid_capture.get(3));
	int frame_height = static_cast<int>(vid_capture.get(4));

	Size frame_size(frame_width, frame_height);

    int count = -1;
    auto start = chrono::system_clock::now();

    while (vid_capture.isOpened())
    {
 
        Mat frame;
        ++count;
        bool isSuccess = vid_capture.read(frame);

        if (isSuccess == false)
        {
            cout << "Video camera is disconnected" << endl;
            break;
        }
        
        if(isSuccess == true)
        {
            
            imshow("Frame", frame);

            string name = "mask_" + to_string(count) + ".png";
            // Replace path_to_store with the folder where you want to store the image
            imwrite(path_to_store + name, frame);

            int key = waitKey(1);

            if (key == 'q')
            {
            cout << "Stopping the video" << endl;
            break;
            }

        }
    }

    auto end = chrono::system_clock::now();

    // calculate the time taken
    chrono::duration<double> elapsed_seconds = end-start;
    cout << elapsed_seconds.count() << "s" << endl;

    destroyAllWindows();
    vid_capture.release();
   
   return 0;
}

