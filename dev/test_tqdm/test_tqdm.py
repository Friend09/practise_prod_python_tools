# import time
# import tqdm

# for outer in tqdm.tqdm([10,20,30,40,50], desc="Outer: ", position=0):
#     for inner in tqdm.tqdm(range(outer), desc="Inner: ", position=1, leave=False):
#         time.sleep(0.05)

# print("done!")

import time
import tqdm
import glob

pbar = tqdm.tqdm(glob.glob("./dev/test_tqdm/*.txt"))
for file in pbar:
    pbar.set_description(file)
    time.sleep(.5)
