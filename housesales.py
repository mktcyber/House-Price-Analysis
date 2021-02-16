import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits
import matplotlib

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import ensemble

class House(object):
    def __init__(self):
        print("Loading CSV file...")
        self.data = pd.read_csv("kc_house_data.csv")
        print("CSV file Loaded.")
        

    def train_model(self):
        print("Training model... (Might Take Time)")
        self.reg = LinearRegression()
        labels = self.data['price']
        conv_dates = [1 if values == 2014 else 0 for values in self.data.date ]
        self.data['date'] = conv_dates
        train1 = self.data.drop(['id', 'price'],axis=1)
        self.x_train , self.x_test , self.y_train , self.y_test = train_test_split(train1 , labels , test_size = 0.10,random_state =2)
        self.reg.fit(self.x_train,self.y_train)
        # self.reg.score(self.x_test,self.y_test)

        self.clf = ensemble.GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2, learning_rate = 0.1, loss = 'ls')
        self.clf.fit(self.x_train, self.y_train)
        # self.clf.score(self.x_test,self.y_test)

    def get_model_score(self, model_type):
        if(model_type == 'LR'):
            score = np.around((self.reg.score(self.x_test,self.y_test)*100), 2)
            return score

        elif(model_type == 'GBR'):
            score = np.around((self.clf.score(self.x_test,self.y_test)*100), 2)
            return score

    def predict(self, model_type, *params):

        data_dict = [{'date':params[0],
                      'bedrooms':params[1],
                      'bathrooms':params[2],
                      'sqft_living':params[3],
                      'sqft_lot':params[4],
                      'floors':params[5],
                      'waterfront':params[6],
                      'view':params[7],
                      'condition':params[8],
                      'grade':params[9],
                      'sqft_above':params[10],
                      'sqft_basement':params[11],
                      'yr_built':params[12],
                      'yr_renovated':params[13],
                      'zipcode':params[14],
                      'lat':params[15],
                      'long':params[16],
                      'sqft_living15':params[17],
                      'sqft_lot15':params[18]
                      }]
        # i=0
        # for key in data_dict:
        #     data_dict[key] = params[i]
        #     i+=1

        predict_df = pd.DataFrame(data_dict)
        
        if(model_type == 'LR'):
            y_p = np.around(self.reg.predict(predict_df), 2)
            return y_p[0]

        elif(model_type == 'GBR'):
            y_p = np.around(self.clf.predict(predict_df), 2)
            return y_p[0]


    def bedrooms(self):
        self.data['bedrooms'].value_counts().plot(kind='bar')
        plt.title('number of Bedroom')
        plt.xlabel('Bedrooms')
        plt.ylabel('Count')
        plt.show()

    def floors(self):
        self.data['floors'].value_counts().plot(kind='bar')
        plt.title('number of Floors')
        plt.xlabel('Floors')
        plt.ylabel('Count')
        plt.show()

    def geography(self):
        plt.figure(figsize=(10,10))
        sns.jointplot(x=self.data.lat.values, y=self.data.long.values, height=10)
        plt.ylabel('Longitude', fontsize=12)
        plt.xlabel('Latitude', fontsize=12)
        plt.show()
        

    def price_square_feet(self):
        plt.scatter(self.data.price, self.data.sqft_living)
        plt.ylabel("Price")
        plt.xlabel('square feet')
        plt.title("Price vs Square Feet")
        plt.show()

    def longitude_price(self):
        plt.scatter(self.data.long, self.data.price)
        plt.ylabel("longitude")
        plt.xlabel('price')
        plt.title("Price vs longitude of the area")
        plt.show()

    def latitude_price(self):
        plt.scatter(self.data.lat,self.data.price)
        plt.xlabel("latitude")
        plt.ylabel('price')
        plt.title("Latitude vs Price")
        plt.show()

    def bedrooms_price(self):
        plt.scatter(self.data.bedrooms,self.data.price)
        plt.title("Bedroom and Price ")
        plt.xlabel("Bedrooms")
        plt.ylabel("Price")
        plt.show()
        sns.despine

    def waterfront_price(self):
        plt.scatter(self.data.waterfront,self.data.price)
        plt.xlabel("waterfront")
        plt.ylabel("Price")
        plt.title("Waterfront vs Price ")
        plt.show()

    def floors_price(self):
        plt.scatter(self.data.floors,self.data.price)
        plt.xlabel("Floors")
        plt.ylabel("Price")
        plt.show()
        

    def zipcode_price(self):
        plt.title("Which is the pricey location by zipcode?")
        plt.scatter(self.data.zipcode,self.data.price)
        plt.xlabel("zipcode")
        plt.ylabel("Price")
        plt.show()

    def find_values(self, category, input):
        count_df = self.data[category] == float(input)
        count = self.data[count_df]
        return count.shape[0]

    
        

if __name__ == "__main__":
    H = House()
    H.geography()


