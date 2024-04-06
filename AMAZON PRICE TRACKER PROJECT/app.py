from flask import Flask
from flask import render_template,request,redirect,url_for
from Data_Scraper import fatch_product_detils,auto_scrapper
from Methods import Chart_Generator,Filter_data,Filter_data_available_prod,Get_All_Available_Product,Get_All_Data
from Methods import Get_All_Praticlar_Labels,Get_All_Praticlar_Prices,Get_Particular_Product

app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ASIN_SORT = request.form['prod_asin_sort']
        Product_Name = request.form['prod_asin_scrap']
        Btn_name_manual_scrap = request.form.get('manual scrap')
        Btn_name_available_product = request.form.get('Avaliable Product')

        if(ASIN_SORT):
            row = Filter_data(ASIN_SORT)
            return render_template('index.html', rows = row)
        elif(Product_Name):
            print(Product_Name)
            fatch_product_detils(Product_Name)
            row = Get_All_Data()
            return render_template('index.html', rows = row)
        elif(Btn_name_manual_scrap):
            auto_scrapper()
            row = Get_All_Data()
            return render_template('index.html', rows = row)
        elif(Btn_name_available_product):
            return redirect(url_for('Available_Product'))
        else:
            row = Get_All_Data()
            return render_template('index.html', rows = row)
    
    else:
        row = Get_All_Data() 
        return render_template('index.html', rows = row)


@app.route("/Display_Product/<asin>", methods=['POST','GET'])
def Display_Product(asin):
    if request.method == 'POST':
        RESET_TABLE = request.form.get('reset table')
        MANUAL_SCRAP = request.form.get('manual scrap')
        PRODUCT_NAME = request.form['prod_asin_scrap']
        if request.method == 'POST':
            if(RESET_TABLE):
                return redirect(url_for('home'))
            elif(MANUAL_SCRAP):
                auto_scrapper()
                return redirect(url_for('home'))
            elif(PRODUCT_NAME):
                fatch_product_detils(PRODUCT_NAME)
                return redirect(url_for('Available_Product'))
            else:
                return redirect(url_for('Available_Product'))
    else:
        row = Get_Particular_Product(asin)
        date = Get_All_Praticlar_Labels(asin)
        price = Get_All_Praticlar_Prices(asin)
        return render_template('Display Product.html',rows=row, image_filename=Chart_Generator(date,price))

@app.route('/Available_Product', methods=['POST','GET'])
def Available_Product():
    if request.method == 'POST':
        ASIN_SORT = request.form.get('prod_asin_sort')
        RESET_TABLE = request.form.get('reset table')
        MANUAL_SCRAP = request.form.get('manual scrap')
        PRODUCT_NAME = request.form['prod_asin_scrap']
        if(ASIN_SORT):
            row = Filter_data_available_prod(ASIN_SORT)
            return render_template('Avaliable Product.html', rows = row)
        elif(RESET_TABLE):
            return redirect(url_for('home'))
        elif(MANUAL_SCRAP):
            auto_scrapper()
            return redirect(url_for('home'))
        elif(PRODUCT_NAME):
            fatch_product_detils(PRODUCT_NAME)
            row = Get_All_Available_Product()
            return render_template('Avaliable Product.html',rows = row)
        else:
            row = Get_All_Available_Product()
            return render_template('Avaliable Product.html',rows = row)
    else:
        row = Get_All_Available_Product()
        return render_template('Avaliable Product.html',rows = row)

if __name__ == '__main__':
    app.run(debug=True)