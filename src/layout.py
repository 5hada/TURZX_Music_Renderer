from data import Rect, Layout, PointRect
from constants import MODE, H, W, PAD_X, PAD_Y, SPACE_X as SPC_X, SPACE_Y as SPC_Y, THUMB_W as TMB_W, THUMB_H as TMB_H, TITLE_H, DETAIL_H, PROGRESS_H as PRG_H, TIME_W, TIME_H

CUR_W = W if MODE == 'portrait' else H
CUR_H = H if MODE == 'portrait' else W

def ThumbNailRect() -> Rect:
    return Rect(PAD_X, PAD_Y, TMB_W, TMB_H)

def TitleRect(tmb: Rect) -> Rect:
    x:int = PAD_X + tmb.w + SPC_X
    return Rect(x, PAD_Y, CUR_W-x-PAD_X, TITLE_H)

def DetailRect(title: Rect) -> Rect:
    return Rect(title.x, title.y + title.h + SPC_Y, title.w, DETAIL_H)

def TimeStampRect(tmb: Rect) -> Rect:
    return Rect(tmb.x, tmb.y + tmb.h + SPC_Y, TIME_W, TIME_H)

def ProgressRect(time: Rect) -> Rect:
    x:int = time.x + SPC_X + time.w
    return Rect(x, time.y, CUR_W - 2*x, PRG_H)

def TotalTimeRect(time: Rect) -> Rect:
    return Rect(CUR_W - (time.x + time.W), time.y, time.w, time.h)

def BackgroundRects(areas: list[Rect], total: Rect) -> list[Rect]:
    grid_x: list[int] = [].extend([0, CUR_W])
    grid_y: list[int] = [].extend([0, CUR_H])
    for area in areas:
        grid_x.extend([area.left, area.right])
        grid_y.extend([area.top, area.bottom])
    grid_x, grid_y = list(set(grid_x)), list(set(grid_y))
    grid_x.sort()
    grid_y.sort()
    len_x: int = len(grid_x) - 1
    len_y: int = len(grid_y) - 1

    blanks: list[PointRect] = []
    for xi in range(len_x):
        for yi in range(len_y):
            box: PointRect = PointRect([grid_x[xi], grid_y[yi]], [grid_x[xi+1], grid_y[yi+1]])

            isInArea: bool = False
            for area in areas:
                if area >= box.rect:
                    isInArea = True
            if isInArea:
                continue
            blanks.append(box)



    back_areas: list[Rect] = []

    return back_areas


def GetLayout() -> Layout:
    tmb: Rect = ThumbNailRect()
    title: Rect = TitleRect(tmb)
    detail: Rect = DetailRect(title)
    time: Rect = TimeStampRect(tmb)
    prg: Rect = ProgressRect(time)
    total: Rect = TotalTimeRect(time)
    back: list[Rect] = BackgroundRects(list[tmb, title, detail, prg, time], total)
    return Layout(tmb, title, detail, prg, time, total, back)
