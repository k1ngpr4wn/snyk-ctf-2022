FROM python:3
RUN wget https://nodejs.org/dist/v18.12.1/node-v18.12.1-linux-x64.tar.xz && tar xf node-v18.12.1-linux-x64.tar.xz && rm node-v18.12.1-linux-x64.tar.xz
ENV PATH="$PATH:/node-v18.12.1-linux-x64/bin"
RUN pip3 install flask requests
RUN apt-get update && apt-get install -y libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxcomposite1 libxdamage1 libxfixes3 libgbm1 libxkbcommon0 libasound2 libxrandr2
RUN useradd -m app
RUN mkdir /app && chown -R app:app /app
WORKDIR /app
USER app
RUN npm install -g puppeteer
ADD . /app
EXPOSE 5000
ENTRYPOINT flask run -h 0.0.0.0