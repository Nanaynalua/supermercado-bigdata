FROM node:20

WORKDIR /app
RUN npm install -g create-react-app
RUN create-react-app supermercado-frontend
WORKDIR /app/supermercado-frontend
RUN npm install axios chart.js react-chartjs-2

EXPOSE 3000
CMD ["npm", "start"]
