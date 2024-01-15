# TL;DR
Repository of `Jupyter notebooks` for the 2018 PyCon talk:
*A practical guide to Singular Value Decomposition in Python* by Daniel
Pyrathon.[^1][^2][^3]

## Docker
Below we discuss how to run the `Jupyter notebooks` using **Docker**:

### Development
To run the notebooks locally, and persist changes made to the notebooks, first
`git clone` the repo:
```
git clone https://github.com/RagingTiger/Singular-Value-Decomposition-PyCon2018.git
```
Then `cd Singular-Value-Decomposition-PyCon2018` and run the following:
```
docker run -d \
           --rm \
           --name SVD \
           -e JUPYTER_ENABLE_LAB=yes \
           -p 8888:8888 \
           -v $PWD:/home/jovyan \
           ghcr.io/ragingtiger/singular-value-decomposition-pycon2018:master && \
sleep 5 && \
docker logs SVD 2>&1 | grep "http://127.0.0.1" | tail -n 1 | awk '{print $2}'
```
Click the link (should look similar to:
http://127.0.0.1:8888/lab?token=LONG_ALPHANUMERIC_STRING) which will
`automatically` log you in and allow you to start running the *notebooks*.

## References
[^1]: [PyCon 2018 Talk](https://youtu.be/d7iIb_XVkZs)
[^2]: [PyCon 2018 Slides](https://speakerdeck.com/pycon2018/daniel-pyrathon-a-practical-guide-to-singular-value-decomposition-in-python)
[^3]: [Surprise SVD Docs](https://surpriselib.com/)
