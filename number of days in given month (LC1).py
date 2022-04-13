{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMhyeF7v1V1jKwrFZD+Dre6",
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
        "<a href=\"https://colab.research.google.com/github/AbbasShaik786/AbbasShaik786/blob/main/number%20of%20days%20in%20given%20month%20(LC1).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "czfIER0e53WW",
        "outputId": "ae6dd790-f649-46c7-b730-1dfad228b39f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter the month3\n",
            "entered month is 3\n",
            "no of days:31\n"
          ]
        }
      ],
      "source": [
        "x = int(input(\"enter the month\"))\n",
        "print(\"entered month is\",x)\n",
        "if x in (1,3,5,7,8,10,12):\n",
        "  print(\"no of days:31\")\n",
        "elif x in (4,6,9,11):\n",
        "  print(\"no of days:30\")\n",
        "else:\n",
        "  print(\"28 days\")"
      ]
    }
  ]
}