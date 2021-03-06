import csv

def triangleArea(points):
    area = 0.5 * abs((abs(points[1][0] - points[0][0]) * abs(points[2][1] - points[0][1])) - (abs(points[2][0] - points[0][0]) * abs(points[1][1] - points[0][1])))
    return area

def cityArea(city):
    w = abs(float(city['TopLeft_X']) - float(city['BottomRight_X']))
    h = abs(float(city['TopLeft_Y']) - float(city['BottomRight_Y']))
    return w * h

def triangleAreaSum(city,point):
    a = [float(city['TopLeft_X']) , float(city['TopLeft_Y'])]
    b = [float(city['BottomRight_X']), float(city['TopLeft_Y'])]
    c = [float(city['TopLeft_X']), float(city['BottomRight_Y'])]
    d = [float(city['BottomRight_X']), float(city['BottomRight_Y'])]
    point = [float(point['X']),float(point['Y'])]
    area_sum = triangleArea([a,point,d]) + triangleArea([d,point,c]) + triangleArea([c,point,b]) + triangleArea([point,b,a])
    return area_sum



with open('cities.csv') as f:
    cities = [city for city in csv.DictReader(f)]

with open('points.csv') as f:
    points = [point for point in csv.DictReader(f)]


for point in points:
    flag = True
    for city in cities:
        city_area = cityArea(city)
        triangles_sum = triangleAreaSum(city,point)
        if triangles_sum > city_area:
            pass
        else:
            flag = False
            point['City'] = city['Name']
            break
    if flag:
        point['City'] = 'None'

with open('output_points.csv', 'w') as f:
    fieldnames = ['ID', 'X', 'Y', 'City']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(points)