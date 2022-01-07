# Pre-processing for Telegram Sticker Packs

## usage

### directory structure

```
|-[sticker_folder_name]
| |-input
| | |-*.{jpg,png}
| |-output
|   |-(products)
|-convert_resize.py
|-check.py
|-create_icon.py
```

### convert & resize

```bash
python convert_resize.py [sticker_folder_name]
```

### check the size and format

```bash
python check.py [sticker_folder_name]/output/
```

### create icon

```bash
python create_icon [icon_picture_path]
```
