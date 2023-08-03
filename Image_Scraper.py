import requests
import shutil

# Opening SKU TXT File For Prep #
skus = open('SKUs.txt', 'r')
read_skus = skus.readlines()

# Depending on how many images a product has, it may be possible to gather more than one image of a product at a time
# product_image_count is which image in the rotation that it starts and image_cap is the image that it stops the rotation
product_image_count = 1
image_cap = 10

# For Reading Text File #
for x in read_skus:
    # Attempting Image Count Test #
    try:
        while product_image_count <= image_cap:
            try:
                # Setting up Photo Placement and Image URL #
                product_image_placement = product_image_count
                product_sku = x.strip()
                url="https://WEBSITE.com/Product%20Images/"+product_sku+"/"+product_sku+"_0"+str(product_image_placement)+".jpg"
                image_filename = f"{product_sku}_0{product_image_placement}.jpg"

                # Attempting Saved Image Path and Image Saving #
                try:
                    save_path = "C:\\Users\\PATH\\TO\\IMAGES\\FOLDER"
                    res = requests.get(url, stream = True)
                    print("Save Path and Request Set...")

                    # Image Checking & Image Placement Check #
                    if res.status_code == 200 and product_image_count < 5:
                        with open(image_filename, 'wb') as f:
                            shutil.copyfileobj(res.raw, f)
                        product_image_count += 1
                        # Successful Run Message #
                        print('Image sucessfully Downloaded: ', image_filename)
                    
                    elif product_image_count >= 5:
                        # Product Image Placement Reset #
                        product_image_count = 1
                        break

                    else:
                        # Image Couldn't Be Retreived #
                        print(f'Image {image_filename} Couldn\'t be retrieved')
                        product_image_count = 1
                        break
                    
                    files = r"C:\\Users\\PATH\\TO\\Image_Scraper FOLDER"
                    for f in files:
                        src = files+image_filename
                        save_path = r"C:\\Users\\SAVE\\TO\\IMAGES\\FOLDER\\"
                        try:
                            print("Move Attempt Started...")
                            print("Source: "+src+"\nSave Path: "+save_path)
                            shutil.move(src, save_path)
                            print("Move Attempt Successful!")
                        except Exception as e:
                            print("Move Attempt Failed due to "+str(e))
                            break

                except Exception as e:
                    # URL Is Invalid #
                    print('Error: ' + str(e))
                    break

            except:
                # No Product Image #
                print("Error: No Product Image for", product_sku, ". Please try again")

    # Image Count Failed #
    except:
        # Image not saved to Correct Folder #
        print("error: image not sent to FOLDER_NAME folder.")
        continue
