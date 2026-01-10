#include <windows.h>

extern "C" __declspec(dllexport)

int get_pixel(int x, int y, int* out_rgb)
{
    HDC dng = GetDC(NULL);
    COLORREF c = GetPixel(dng, x, y);

    out_rgb[0] = GetRValue(c);
    out_rgb[1] = GetGValue(c);
    out_rgb[2] = GetBValue(c);

    ReleaseDC(NULL, dng);
    return 0;
}
