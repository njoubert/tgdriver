# Frontend server instructions

Run 

    python3 preprocess_kml.py 9090 > brcmap_preprocessed.kml

to generate a KML version where file are fetched from localhost:9090.
The script will download and cache the content under the static folder.
