###这里都是文档给的置换表
IP_sub = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12,  4,62, 54, 46, 38, 30, 22, 14,  6, 64, 56, 48, 40, 32, 24, 16,  8,57, 49, 41, 33, 25, 17,  9,  1, 59, 51, 43, 35, 27, 19, 11,  3,61, 53, 45, 37, 29, 21, 13,  5, 63, 55, 47, 39, 31, 23, 15,  7]
IP_inver_sub = [40,  8, 48, 16, 56, 24, 64, 32, 39,  7, 47, 15, 55, 23, 63, 31,38,  6, 46, 14, 54, 22, 62, 30, 37,  5, 45, 13, 53, 21, 61, 29,36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,  9, 49, 17, 57, 25]
Key_sub_1 = [57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4]
Key_sub_2 = [14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
Key_Extension =[32,  1,  2,  3,  4,  5,  4,  5,  6,  7,  8,  9,
 8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32,  1 ];
Key_left = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1];
Pbox = [16,  7, 20, 21, 29, 12, 28, 17,  1, 15, 23, 26,  5, 18, 31, 10,
 2,  8, 24, 14, 32, 27,  3,  9, 19, 13, 30,  6, 22, 11,  4, 25];
Sbox1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]];
Sbox2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]];
Sbox3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]];
Sbox4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]];
Sbox5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]];
Sbox6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]];
Sbox7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]];
Sbox8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]];
R_E = [0]*48;###R_E是Ri经过E盒扩展后的东西
###
def output_48(binary):###debug方便写的一个输出函数
    print("0x", end='');
    for i in range(12):  ###从头开始直接以四个为一个单位打出来
        result = 0;
        A = 1;
        for j in range(4):
            result += A * binary[i * 4 + 3 - j];  ###四个一组，每组从右边开始数
            A *= 2;
        if (result < 10):
            print(result, end='');
        else:
            print(chr(97 + result - 10), end='');
def output_32(binary):###debug方便写的一个输出函数
    print("0x", end='');
    for i in range(8):  ###从头开始直接以四个为一个单位打出来
        result = 0;
        A = 1;
        for j in range(4):
            result += A * binary[i * 4 + 3 - j];  ###四个一组，每组从右边开始数
            A *= 2;
        if (result < 10):
            print(result, end='');
        else:
            print(chr(97 + result - 10), end='');
def output_4(binary):###debug方便写的一个输出函数
    print("0x", end='');
    for i in range(1):  ###从头开始直接以四个为一个单位打出来
        result = 0;
        A = 1;
        for j in range(4):
            result += A * binary[i * 4 + 3 - j];  ###四个一组，每组从右边开始数
            A *= 2;
        if (result < 10):
            print(result, end='');
        else:
            print(chr(97 + result - 10), end='');
def IP(a,c):###按照c对a进行 64 位IP置换，或者反置换
    b = [0]*64;
    for i in range(64):
        b[i] = a[c[i]-1];###注意减1，因为数组是从零开始
    return b;
def PC(a,c):###用于生成 56 位密钥的置换1,按照c对a
    b = [0]*56;
    for i in range(56):
        b[i] = a[c[i]-1];###注意减1，因为数组是从零开始
    return b;
def PC_1(a,c):###用于产生 48 位密钥的置换2
    b = [0]*48;
    for i in range(48):
        b[i] = a[c[i]-1];###注意减1，因为数组是从零开始
    return b;
def Pbox_func(a,c):###用于产生 32 位密钥的Pbox
    b = [0]*32;
    for i in range(32):
        b[i] = a[c[i]-1];###注意减1，因为数组是从零开始
    return b;
def left_move(a,lenth_a,loop):###这是进行循环左移的函数，loop是指循环几次
    if(loop==1):
        temp = a[0];
        for i in range(lenth_a-1):
            a[i] = a[i+1];
        a[lenth_a-1] = temp;
    elif(loop==2):
        temp1 = a[0];
        temp2 = a[1];
        for i in range(lenth_a-2):
            a[i] = a[i+2];
        a[lenth_a-2] = temp1;
        a[lenth_a-1] = temp2;
    return a;
def XOR(a,b):###XOR是异或操作
    lenth = len(a);
    c = [0]*lenth;
    for i in range(lenth):
        c[i] = a[i]^b[i];
    return c;
def Sbox_func(a,box):###Sbox压缩操作
    row = 2*a[0]+a[5];
    column = 8*a[1]+4*a[2]+2*a[3]+a[4];
    num = box[row][column];#行列都是从零开始的
    line = [0]*4;
    for i in range(4):##将压缩的四位数字，以1011为例，分别存在了数组的 0 1 2 3的位置上
        line[3-i] = num%2;
        num = num//2;
    return line;
def circulate(L_0,R_0):##该函数是用来循环轮数的框架
    R = [([0] * 32) for i in range(17)];
    L = [([0] * 32) for i in range(17)];
    L[0] = L_0;
    R[0] = R_0;
    for i in range(16):
        L[i+1] = R[i];
        R[i+1] = XOR(L[i],F(R[i],i));
    # output_32(R[1]);
    # print("");
    #print(f"L[1]={L[1]}");
    LR = [0]*64;
    LR[0:32] = R[16];
    LR[32:64] = L[16];
    #output(LR);
    return LR;
def F(R,i):#F是轮函数
    R_E = PC_1(R,Key_Extension);
    AfterE = XOR(R_E,PC_1(Key_sum[i],Key_sub_2));##AfterE是对应在异或的操作上，S盒压缩的上面.48位
    #这说明我的所有K是对的
    # if(i==15):
    #     print(Key_sum[0][28]);
    #     print("");
    #     print("这是K16:",end=' ');
    #     output(PC_1(Key_sum[15],Key_sub_2));
    arr = [0]*32;
    arr[0:4] = Sbox_func(AfterE[0:6],Sbox1);
    arr[4:8] = Sbox_func(AfterE[6:12],Sbox2);
    arr[8:12] = Sbox_func(AfterE[12:18],Sbox3);
    arr[12:16] = Sbox_func(AfterE[18:24],Sbox4);
    arr[16:20] = Sbox_func(AfterE[24:30],Sbox5);
    arr[20:24] = Sbox_func(AfterE[30:36],Sbox6);
    arr[24:28] = Sbox_func(AfterE[36:42],Sbox7);
    arr[28:32] = Sbox_func(AfterE[42:48],Sbox8);
    # if(i==0):
    #     for l in range(8):
    #         output_4(arr[l*4:(l+1)*4]);
    #         print("");
    arr = Pbox_func(arr,Pbox);
    return arr;
def twoarr(c,d):###在python里面还是，用函数给二维数组赋值 不会出错
    cd_pin = [0]*56;
    cd_pin[0:28] = c;
    cd_pin[28:56] = d;
    return cd_pin;
def sixteen_put(binary):###这个函数是将一个二进制数组转化为十六进制输出
    print("0x", end='');
    for i in range(16):  ###从头开始直接以四个为一个单位打出来
        result = 0;
        A = 1;
        for j in range(4):
            result += A * binary[i*4+3-j];###四个一组，每组从右边开始数
            A *= 2;
        if (result < 10):
            print(result,end='');
        else:
            print(chr(97+result-10),end='');

###因为main是个函数的缘故，所以要把Key_sum放到全局变量上面
Key_sum = [([0]*56)for i in range(16)];
def main():
    line_1 = input().strip();
    line_2 = input().strip();
    line_3 = input().strip();
    line_4 = input().strip();
    T = int(line_1);
    s = int(line_2,16);
    k = int(line_3,16);
    op = int(line_4);

    s_2 = [0]*64;#s_2是存64位明文
    k_2 = [0]*64;#k_2是64位的密钥
    for i in range(64):
        s_2[63-i] = s%2;
        s = s//2;
    for i in range(64):
        k_2[63-i] = k%2;
        k = k//2;
    ##这一步将明密文都转化成了2进制数字组


    s_2 = IP(s_2,IP_sub);
    ###s_2 初始IP置换成功

    l_0=s_2[0:32];
    r_0=s_2[32:64];
    ###R L分完

    k_3 = [0]*56;
    k_3 = PC(k_2,Key_sub_1);
    ###k_3 = 64位变56位密钥 和 第一次置换
    #print(f"密钥K 56位是：{k_3}");
    c = [0]*16*28;
    d = [0]*16*28;
    c_1 = [0] * 28;
    d_1 = [0] * 28;

    ###28位密钥分完
    c_1 = k_3[0:28];
    d_1 = k_3[28:56];
    C=[];
    D=[];
    cd = [0]*48;###cd是cd_pin第二次置换后，成为48位的
    for i in range(16):
        c[i*28:(i+1)*28] = left_move(c_1, 28, Key_left[i]);#c[0-27]存的是第一次左移后的
        # print(f"c{i} = ",end='');
        # output(c[i*28:(i+1)*28]);
        # print("");
        d[i*28:(i+1)*28] = left_move(d_1, 28, Key_left[i]);
        # print(f"d{i} = ", end='');
        # output(d[i * 28:(i + 1) * 28]);
        # print("");
        c_1 = c[i*28:(i+1)*28];
        d_1 = d[i*28:(i+1)*28];
        C.append(c[i*28:(i+1)*28]);
        D.append(d[i*28:(i+1)*28]);
    # 完成了循环左移,CD中存下了1-16轮的左右密钥，即ci di
    ###经验证，密钥c0-c16,d0-d16均正确,我的代码中c0表示理论的c1

    if(op==1):
        for i in range(16):
            Key_sum[i] = twoarr(C[i],D[i]);
    else:
        for i in range(16):
            Key_sum[15-i] = twoarr(C[i], D[i]);
    #print(Key_sum[15]);###Key_sum按顺序存放了16轮56位密钥，这一步是对的
    #######
    #######以上部分完成了密钥的存放

    result_arr = [0]*64;
    for i in range(T):
        result_arr = circulate(l_0, r_0);
        result_arr = IP(result_arr,IP_inver_sub);
        result_arr = IP(result_arr,IP_sub);###因为涉及到要进行IP置换，随后分成L0R0，所以要在这一步加上来。
        l_0 = result_arr[0:32];
        r_0 = result_arr[32:64];
        if(i!=T-1):
            result_arr = [0]*64;
    result_arr = IP(result_arr,IP_inver_sub);###这里是因为for循环是以IP置换后为结尾的，所以我要是想得到一般的arr，肯定还要逆置换回来
    #print(result_arr);
    sixteen_put(result_arr);

if __name__ == "__main__":
    main()



