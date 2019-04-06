
#pragma once

// The following macros define the minimum required platform.  The minimum required platform
// is the earliest version of Windows, Internet Explorer etc. that has the necessary features to run
// your application.  The macros work by enabling all features available on platform versions up to and
// including the version specified.

// Modify the following defines if you have to target a platform prior to the ones specified below.
// Refer to MSDN for the latest info on corresponding values for different platforms.
#ifndef _WIN32_WINNT        // Specifies that the minimum required platform is Windows Vista.
#define _WIN32_WINNT 0x0600 // Change this to the appropriate value to target other versions of Windows.
#endif

#include "./Include/CLEyeMulticam.h"
#include "iostream"
#include "Windows.h"

using namespace std;
extern "C" int topla()
{
    int a = 3;
    int b = 2;
    return CLEyeGetCameraCount();
}

extern "C" GUID getUid()
{
    return CLEyeGetCameraUUID(0);
}

extern "C" int run()
{
    GUID guid;
    PBYTE pCapBuffer = NULL;
    cout << "I am counting this much cam:";
    cout << CLEyeGetCameraCount() << "\n";
    guid = CLEyeGetCameraUUID(0);
    printf("Camera %d GUID: [%08x-%04x-%04x-%02x%02x-%02x%02x%02x%02x%02x%02x]\n",
           0, guid.Data1, guid.Data2, guid.Data3,
           guid.Data4[0], guid.Data4[1], guid.Data4[2],
           guid.Data4[3], guid.Data4[4], guid.Data4[5],
           guid.Data4[6], guid.Data4[7]);
    CLEyeCameraInstance cam = CLEyeCreateCamera(guid, rand() < (RAND_MAX >> 1) ? CLEYE_COLOR_PROCESSED : CLEYE_MONO_PROCESSED,
                                                rand() < (RAND_MAX >> 1) ? CLEYE_VGA : CLEYE_QVGA, 30);
    if (cam)
        cout << "Kamera Olusturuldu\n";

    if (CLEyeCameraLED(cam, true))
        cout << "Led Yandi\n";
    if (CLEyeCameraStart(cam))
        cout << "Kamera Calisti\n";
    if (CLEyeCameraGetFrame(cam, pCapBuffer))
        cout << "Capture Basarili\n";
    if (CLEyeCameraStop(cam))
        cout << "Kamera Durdu\n";
    return 0;
}
