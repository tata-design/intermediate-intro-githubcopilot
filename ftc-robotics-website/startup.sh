#!/bin/bash
cd /home/site/wwwroot
python -m streamlit run src/home.py --server.port 8000 --server.address 0.0.0.0 --server.headless true
