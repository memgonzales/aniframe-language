FROM nikolaik/python-nodejs:python3.10-nodejs16-bullseye

COPY . /app
WORKDIR /app/browser/p5-widget/p5.js-widget

RUN set -ex 

# Install p5.js widget-related dependencies
RUN npm install

# Install AniFrame interpreter-related dependencies
RUN python3 -m pip install antlr4-python3-runtime==4.13.1 antlr4-tools==0.2.1

# Install AniFrame browser-related dependencies
RUN cd /app/browser/aniframe \
  && python3 -m pip install --no-cache-dir -r requirements.txt \
  && python3 manage.py makemigrations \
  && python3 manage.py migrate \
  && cd frontend \
  && npm install \
  && npm run build

# Port 8080 is used by the p5.js widget embedded in the AniFrame browser
# Port 8000 is used by the AniFrame browser
EXPOSE 8080 8000

CMD ["npm", "start"]