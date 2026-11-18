"""Step 5 (CO2): Stable Diffusion picture with an AI watermark."""
from functools import lru_cache

from .config import DIFFUSION_MODEL, IMAGE_SIZE, WATERMARK_TEXT


@lru_cache(maxsize=1)
def fnGetDiffusion():
    import torch
    from diffusers import StableDiffusionPipeline
    boolGpu = torch.cuda.is_available()
    objPipe = StableDiffusionPipeline.from_pretrained(
        DIFFUSION_MODEL, torch_dtype=torch.float16 if boolGpu else torch.float32)
    return objPipe.to("cuda" if boolGpu else "cpu")


def fnAddWatermark(objImg):
    """Draw the visible AI watermark (dark shadow + white text)."""
    from PIL import ImageDraw
    objDraw = ImageDraw.Draw(objImg)
    objDraw.text((11, IMAGE_SIZE[1] - 19), WATERMARK_TEXT, fill=(0, 0, 0))
    objDraw.text((10, IMAGE_SIZE[1] - 20), WATERMARK_TEXT, fill=(255, 255, 255))
    return objImg


def fnIllustrate(strTitle):
    """Draw a simple travel picture and add the AI watermark."""
    strPrompt = ("Simple travel illustration of " + strTitle +
                 ", flat vector style, no text, clean background")
    objImg = fnGetDiffusion()(strPrompt, height=IMAGE_SIZE[1], width=IMAGE_SIZE[0]).images[0]
    return fnAddWatermark(objImg)
