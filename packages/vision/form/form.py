import os, requests as req
import vision, bucket, base64, time

USAGE = "Please upload a picture and I will tell you what I see"
FORM = [
  {
    "label": "any pics?",
    "name": "pic",
    "required": "true",
    "type": "file"
  },
]

def form(args):
  res = {}
  out = USAGE
  inp = args.get("input", "")
  buc = bucket.Bucket(args)

  if type(inp) is dict and "form" in inp:
    img = inp.get("form", {}).get("pic", "")
    buc = bucket.Bucket(args)
    filename = f"user_image_" + time.strftime("%Y%m%d_%H%M%S") + ".jpg"
    result = buc.write(filename, base64.b64decode(img))
    if result == "OK":
      external_url = buc.exturl(filename, 60*60)
      vis = vision.Vision(args)
      out = vis.decode(img)
      res['html'] = f'<img src="{external_url}">'
    else:
      print(f"Failed to save image: {result}")
      out = "Failed to save image"
  res['form'] = FORM
  res['output'] = out
  return res
