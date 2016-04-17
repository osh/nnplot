#!/usr/bin/env python
#
# NN Plot 
# Tim O'Shea (c) 2016
#
#
#
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

io = [
    ["Input", (2,128)],
    ["Output", (2,128)]
    ]
layers = [
    ['Conv2D(1,1,40)\nLinear', 0.5, 40, 5],
    ['Dense(44)\nRelu', None, 10, 2],
    ['Dense(2*88)\nRelu', None, 15, 3],
    ['Conv2D(1,1,81)\nLinear', 0.5, 40, 5]
    ]

maxy = max(map(lambda x: x[3], layers))
print maxy
fig = plt.figure()
ax = fig.add_subplot(111)
for i,l in enumerate(layers):
    ll=0.25 + i
    w = 0.5
    h = layers[i][3]
    lr=(maxy-h)/2.0

    print (ll,lr,w,h)
    ax.add_patch(
        patches.Rectangle( (ll, lr), w, h, fill=False)
        )
    ax.annotate(l[0], xy=(ll+w/2.0, lr+h/2.0),
        ha='center', va='center',
        rotation=90)

    if(i < len(layers)-1):
    
        h_n = layers[i+1][3]
        lr_n=(maxy-h_n)/2.0
        i_x = ll+w
        o_x = ll+1

        for j in range(0,layers[i][2]):
            for k in range(0,layers[i+1][2]):
                j_rel = (j*1.0/(layers[i][2]-1))
                k_rel = (k*1.0/(layers[i+1][2]-1))
                if(l[1]==None or abs(j_rel - k_rel)<l[1]):
                    i_ht = lr+h*j_rel
                    o_ht = lr_n+h_n*k_rel
                    ax.add_line(lines.Line2D([i_x,o_x], [i_ht,o_ht], color='black', linestyle='solid'))

        if(i == 0):
            for j in range(0,l[2]):
                j_rel = (j*1.0/(l[2]-1))
                ax.add_patch( patches.Circle([i_x-w,lr+h*j_rel], 0.025, color='blue', ec="none") )

        if(i == len(layers)-2):
            for j in range(0,layers[i+1][2]):
                j_rel = (j*1.0/(layers[i+1][2]-1))
                ax.add_patch( patches.Circle([o_x+w,lr_n+h_n*j_rel], 0.025, color='blue', ec="none") )
 
ax.annotate("Inputs (2x128)", xy=(0,maxy/2.0),
        ha='center',va='center',
        rotation=90)
ax.annotate("Outputs (2x128)", xy=(len(layers),maxy/2.0),
        ha='center',va='center',
        rotation=90)

ymarg = 0.05
xmarg = 0.05
plt.ylim(-ymarg, maxy+0.5+ymarg)
plt.xlim(-xmarg,len(layers)+xmarg)
plt.axis('off')
plt.savefig('test.png', bbix_inches='tight')
plt.show()





