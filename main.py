from flask import Flask, render_template, url_for, redirect, request, jsonify 
import pafy
import os


app = Flask(__name__)

desktop = os.path.expanduser("~/Desktop")



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/v/<yid>", methods=['GET', 'POST'])
def download(yid):
    try:
        url = request.form['val']
        ext = request.form['ext']
        
        if ext == "Mp4":
            #url = request.form['val']
            video = pafy.new(url)
            yout_id = video.videoid
            best = video.getbest(preftype="mp4")
            download_url = best.url
            vtitle = video.title
            vdescription = video.description
       


     
            return render_template('info.html', best_url=download_url, vtitle = video.title, vdescription = video.description, vurl = url, yid = yout_id, vext = ext) 
            
        else:
            video = pafy.new(url)
            yout_id = video.videoid
            best = video.getbestaudio()
            download_url = best.url
            vtitle = video.title
            vdescription = video.description

            return render_template('info.html', best_url=download_url, vtitle = video.title, vdescription = video.description, vurl = url, yid = yout_id, vext = ext)
       
        
    except:
        return render_template("error.html")
        

@app.route("/download", methods=['GET', 'POST'])
def downloading():
    try:
        url = request.form['pval']
        ext = request.form['pext']
        if ext == 'Mp4':
            video = pafy.new(url)
            yout_id = video.videoid
            best = video.getbest(preftype="mp4")
            best.download(filepath = desktop)

            return render_template('download.html')
        else:
            video = pafy.new(url)
            yout_id = video.videoid
            best = video.getbestaudio(preftype="m4a")
            best.download(filepath = desktop)

            return render_template('download.html', yid = yout_id)
    except:
        return render_template("error.html")
    
    
    




if __name__ == "__main__":
    app.run(debug=False, port=3000)