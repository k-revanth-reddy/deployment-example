# Deploying Flask Blogging Platform to Vercel

## Prerequisites

1. **GitHub Account**: Your code should be in a GitHub repository
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **MongoDB Atlas Account**: For cloud database (recommended for production)

## Step-by-Step Deployment Process

### Step 1: Prepare Your Database

**Option A: MongoDB Atlas (Recommended for Production)**
1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Create a free cluster
3. Create a database user with read/write permissions
4. Get your connection string
5. Replace `MONGODB_URI` in your environment variables

**Option B: Local MongoDB (Development Only)**
- Not recommended for production as Vercel serverless functions can't connect to local databases

### Step 2: Set Up Environment Variables

1. Go to your Vercel dashboard
2. Select your project
3. Go to Settings → Environment Variables
4. Add the following variables:
   - `SECRET_KEY`: A strong secret key for Flask sessions
   - `MONGODB_URI`: Your MongoDB connection string

### Step 3: Deploy to Vercel

**Method 1: Using Vercel CLI**
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel

# Follow the prompts to connect to your GitHub repo
```

**Method 2: Using Vercel Dashboard**
1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Import your GitHub repository
4. Configure build settings:
   - Framework Preset: Other
   - Build Command: Leave empty
   - Output Directory: Leave empty
   - Install Command: `pip install -r requirements.txt`
5. Add environment variables
6. Deploy

### Step 4: Configure Build Settings

In your Vercel project settings:
- **Build Command**: Leave empty (Vercel will auto-detect)
- **Output Directory**: Leave empty
- **Install Command**: `pip install -r requirements.txt`

### Step 5: Set Up Custom Domain (Optional)

1. In Vercel dashboard, go to Settings → Domains
2. Add your custom domain
3. Configure DNS settings as instructed

## Important Notes

### Database Considerations
- **MongoDB Atlas**: Recommended for production
- **Connection Limits**: Vercel serverless functions have connection limits
- **Connection Pooling**: Consider using connection pooling for better performance

### Environment Variables
Make sure to set these in Vercel:
```
SECRET_KEY=your-strong-secret-key-here
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/blogging_platform?retryWrites=true&w=majority
```

### File Structure
Your project should have:
```
├── app.py              # Main Flask application
├── wsgi.py             # WSGI entry point for Vercel
├── vercel.json         # Vercel configuration
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
└── env.example         # Environment variables example
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are in `requirements.txt`
2. **Database Connection**: Ensure MongoDB Atlas is accessible from Vercel
3. **Environment Variables**: Double-check all variables are set in Vercel dashboard
4. **Build Failures**: Check Vercel build logs for specific error messages

### Performance Optimization

1. **Database Indexing**: Add indexes to frequently queried fields
2. **Connection Pooling**: Use connection pooling for MongoDB
3. **Caching**: Consider implementing Redis for session storage
4. **CDN**: Vercel provides automatic CDN for static assets

## Monitoring

1. **Vercel Analytics**: Monitor performance in Vercel dashboard
2. **MongoDB Atlas**: Monitor database performance
3. **Error Tracking**: Set up error tracking (e.g., Sentry)

## Security Considerations

1. **Environment Variables**: Never commit sensitive data to Git
2. **Database Security**: Use MongoDB Atlas with proper authentication
3. **HTTPS**: Vercel provides automatic HTTPS
4. **Input Validation**: Ensure all user inputs are properly validated

## Post-Deployment

1. **Test All Features**: Verify all functionality works
2. **Set Up Admin User**: Use your setup script to create admin user
3. **Monitor Performance**: Keep an eye on response times and errors
4. **Backup Strategy**: Set up regular database backups 