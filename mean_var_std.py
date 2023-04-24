import numpy as np

def calculate(lst_digits):
    try:
        if len(lst_digits) >= 9:
            arr_3D = np.array(lst_digits).reshape(3, 3)

            cal_format = {
                'mean': [np.mean(arr_3D, axis=0).tolist(), np.mean(arr_3D, axis=1).tolist(), np.mean(arr_3D).item()],
                'variance': [np.var(arr_3D, axis=0).tolist(), np.var(arr_3D, axis=1).tolist(), np.var(arr_3D).item()],
                'standard deviation': [np.std(arr_3D, axis=0).tolist(), np.std(arr_3D, axis=1).tolist(),
                                       np.std(arr_3D).item()],
                'max': [np.max(arr_3D, axis=0).tolist(), np.max(arr_3D, axis=1).tolist(), np.max(arr_3D).item()],
                'min': [np.max(arr_3D, axis=0).tolist(), np.max(arr_3D, axis=1).tolist(), np.max(arr_3D).item()],
                'sum': [np.sum(arr_3D, axis=0).tolist(), np.sum(arr_3D, axis=1).tolist(), np.sum(arr_3D).item()]
            }
            return cal_format
    except ValueError:
        print('List must contain nine numbers')

if __name__=="__main__":
    lst_digits = [0,1,2,3,4,5,6,7,8]
    cal_format = calculate(lst_digits)
    print(cal_format)