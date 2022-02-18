# learning-python
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "datatype.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMgKuL6sFQgV9Nle5RnlDR8",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/badalkchy/Data-type-prac/blob/main/datatype.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "VdJaRNvB9n2_",
        "outputId": "3edd055d-6de3-42c7-987b-42eef21b37b6"
      },
      "source": [
        "a = 'badal'\n",
        "a[0]"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'b'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NEZ62xBC9tW9"
      },
      "source": [
        "b = 'i am badal'\n",
        "c = b[1]"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "vWWLOadu985y",
        "outputId": "37f78ab5-d86c-4f7d-fbe3-dfa060dd1190"
      },
      "source": [
        "c"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "' '"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WMY8NpqT99xo",
        "outputId": "e9be4d9b-6fd1-4d35-b357-f9f3c76424a5"
      },
      "source": [
        "type(c)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pS3lnui_-Bp8",
        "outputId": "99c30eca-80b7-4168-e1c5-966ca92ab288"
      },
      "source": [
        "print(type(c))"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'str'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U5ucJAE3-LS7",
        "outputId": "588b2804-bae9-406c-c054-0f1aff3b9350"
      },
      "source": [
        "d=type(c);\n",
        "print(d);"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'str'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AyDBUEPl-Vir",
        "outputId": "7a1dc61a-0bac-4da9-e84a-f123a4838708"
      },
      "source": [
        "e=type(b);print(e);"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'str'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UVY8d4oM-fdr",
        "outputId": "667b3ba8-c3a2-4b66-ca4a-b06264d111ba"
      },
      "source": [
        "e=type(b)\n",
        "print(e)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'str'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5yVwpT4K-sNK",
        "outputId": "6ca1c404-5264-43f0-c684-4e212c72b5ee"
      },
      "source": [
        "len(b)"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "10"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iEFJR8LI-vNJ",
        "outputId": "a8734dfe-8f13-4c26-d290-681e8f895504"
      },
      "source": [
        "f = 'Man',\"Woman\",\"Male\",\"Female\"\n",
        "g=len(f);\n",
        "print(g);\n",
        "f"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "4\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "('Man', 'Woman', 'Male', 'Female')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iFnUpoD8_bC5",
        "outputId": "7ad81d62-372a-43e5-9fc7-ddfd86375562"
      },
      "source": [
        "len(f[0])"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "mWfO9-59_hzE",
        "outputId": "3ec8096f-e708-4e53-8a1d-2f972e6a3631"
      },
      "source": [
        "f[3]"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Female'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "P2ibUr7fBcfu"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
